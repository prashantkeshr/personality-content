"""Builds the content packs and manifest.json.

python -I tools/build_packs.py <hasaneyldrm exercises.json> <everkinetic exercises.json> <converted illustrations dir>

Sources:
- hasaneyldrm/exercises-dataset: exercise TEXT only (MIT). Its media is
  (c) Gym visual and is not used.
- everkinetic/data: illustrations and text (CC BY-SA 4.0), converted to small
  grayscale PNGs.
- src/authored.py: our own exercises and programs (MIT).
"""

import hashlib
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import authored  # noqa: E402

HY_CREDIT = "Text: exercises-dataset © 2026 Hasan Emir Yıldırım, MIT licence"
EK_CREDIT = "Illustration: Everkinetic (everkinetic.com) by Greg Priday, CC BY-SA 4.0, resized"
EK_TEXT_CREDIT = "Text and illustration: Everkinetic (everkinetic.com) by Greg Priday, CC BY-SA 4.0"
LANGS = ("en", "hi", "es")

# ------------------------------------------------------------------ motions

# Ordered keyword rules: the first match wins. None = no figure (better than a wrong one).
MOTION_RULES = [
    # Moves our figure would show wrongly get no figure instead.
    (r"leg curl|wrist curl|upright row|leg extension|leg press|hip adduct|hip abduct|twist|wood ?chop|rotation|kickback", None),
    (r"hamstring.*stretch|toe touch|forward fold|forward bend", "hamstring_stretch"),
    (r"quad.*stretch", "quad_stretch"),
    (r"calf stretch", "calf_stretch"),
    (r"chest stretch|pec stretch|doorway", "chest_opener"),
    (r"side bend|side stretch|lateral stretch|oblique stretch", "side_bend"),
    (r"stretch", None),
    (r"\bincline push.?up|\bwall push.?up", "incline_push_up"),
    (r"push.?up|press.?up", "push_up"),
    (r"mountain climber", "mountain_climber"),
    (r"burpee", "burpee"),
    (r"jumping jack|star jump", "jumping_jack"),
    (r"high knee", "high_knees"),
    (r"butt kick", "butt_kicks"),
    (r"\bplank", "plank"),
    (r"jump squat|squat jump", "jump_squat"),
    (r"sumo", "sumo_squat"),
    (r"wall sit", "wall_sit"),
    (r"squat|thruster", "squat"),
    (r"reverse lunge", "reverse_lunge"),
    (r"lunge|split squat", "lunge"),
    (r"step.?up", "step_up"),
    (r"calf|heel raise", "calf_raise"),
    (r"good morning", "good_morning"),
    (r"dead.?lift|hip hinge|kettlebell swing|\bswing\b", "hip_hinge"),
    (r"hip thrust|glute bridge|\bbridge\b|hip raise", "glute_bridge"),
    (r"pull.?down", "pulldown"),
    (r"pull.?up|chin.?up", "pull_up"),
    (r"\brow\b|\brows\b|rowing", "row"),
    (r"bench press|chest press|floor press", "bench_press"),
    (r"\bfly\b|\bflye|\bflys\b|crossover", "chest_fly"),
    (r"lateral raise|side raise|lateral delt", "lateral_raise"),
    (r"front raise", "front_raise"),
    (r"shoulder press|overhead press|military press|arnold press|push press", "overhead_press"),
    (r"triceps extension|tricep extension|skull ?crusher|overhead extension|french press", "triceps_extension"),
    (r"\bcurl", "curl"),
    (r"\bdip", "dip"),
    (r"dead bug", "dead_bug"),
    (r"bird dog", "bird_dog"),
    (r"superman|back extension|hyperextension", "superman"),
    (r"leg raise|leg lift|knee raise|flutter kick|scissor", "leg_raise"),
    (r"sit.?up|v.?up|jackknife", "sit_up"),
    (r"crunch", "crunch"),
    (r"shrug", "shoulder_roll"),
    (r"jog|\brun\b|running|sprint", "run"),
    (r"\bwalk", "walk"),
    (r"march", "march"),
    (r"neck", "neck_tilt"),
    (r"cat.?cow|cat stretch|cow stretch", "cat_cow"),
    (r"child", "child_pose"),
    (r"cobra", "cobra"),
    (r"downward dog|down dog", "downward_dog"),
]


def motion_for(name):
    n = name.lower()
    # Machines move the body in ways our figure can't show honestly.
    for pattern, motion in MOTION_RULES:
        if re.search(pattern, n):
            return motion
    return None


def category_for(e):
    n = e["name"].lower()
    if "stretch" in n:
        return "stretching"
    return {
        "waist": "core",
        "cardio": "cardio",
        "neck": "neck",
        "back": "strength",
        "chest": "strength",
        "shoulders": "strength",
        "upper arms": "strength",
        "lower arms": "strength",
        "upper legs": "strength",
        "lower legs": "strength",
    }.get(e.get("body_part"), "generalFitness")


def title(s):
    small = {"and", "with", "on", "of", "to", "in", "the", "a", "or", "v."}
    words = s.replace("_", " ").split()
    return " ".join(w if (i and w in small) else (w[:1].upper() + w[1:]) for i, w in enumerate(words))


# ------------------------------------------------------------------ matching

STOP = {"with", "on", "the", "a", "an", "exercise", "using", "and", "of", "to", "in", "your", "for"}
EQUIP_WORDS = {
    "barbell": "barbell", "barbells": "barbell", "dumbbell": "dumbbell", "dumbbells": "dumbbell",
    "cable": "cable", "machine": "machine", "band": "band", "bands": "band", "kettlebell": "kettlebell",
    "ball": "ball", "smith": "smith", "ez": "barbell",
}


def tokens(name):
    t = re.sub(r"[^a-z0-9 ]", " ", name.lower().replace("-", " ")).split()
    out = set()
    for w in t:
        if w in STOP:
            continue
        w = w[:-1] if w.endswith("s") and len(w) > 3 else w
        out.add(w)
    return out


def equipment_of(toks):
    return {EQUIP_WORDS[w] for w in toks if w in EQUIP_WORDS} or {EQUIP_WORDS.get(w + "s") for w in toks if w + "s" in EQUIP_WORDS} - {None}


def match_illustrations(hy, ek):
    """Pairs each Everkinetic illustration with its closest dataset exercise."""
    hy_t = [(e, tokens(e["name"])) for e in hy]
    pairs = {}
    for k in ek:
        kt = tokens(k["title"])
        best, score = None, 0.0
        for e, et in hy_t:
            if equipment_of(kt) != equipment_of(et):
                continue
            j = len(kt & et) / len(kt | et)
            if j > score:
                best, score = e, j
        if best and score >= 0.75 and best["id"] not in pairs:
            pairs[best["id"]] = k
    return pairs


# ------------------------------------------------------------------ build

def write_zip(path, files):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in files:
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))  # reproducible
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    data = open(path, "rb").read()
    return len(data), hashlib.sha256(data).hexdigest()


def pack_json(pid, version, exercises, programs, credit, license):
    return json.dumps({"id": pid, "version": version, "license": license, "credit": credit,
                       "exercises": exercises, "programs": programs}, ensure_ascii=False, separators=(",", ":"))


def main(hy_path, ek_path, img_dir):
    hy = json.load(open(hy_path, encoding="utf-8"))
    ek = json.load(open(ek_path, encoding="utf-8"))
    ek = [k for k in ek if os.path.exists(os.path.join(img_dir, f"{k['id']}-relaxation.png"))]
    pairs = match_illustrations(hy, ek)
    matched_ek = {k["id"] for k in pairs.values()}

    def images(k):
        return [f"illustrations/{k['id']}-relaxation.png", f"illustrations/{k['id']}-tension.png"]

    library = []
    for e in hy:
        steps = {l: e["instruction_steps"][l] for l in LANGS if e.get("instruction_steps", {}).get(l)}
        if not steps.get("en"):
            continue
        k = pairs.get(e["id"])
        item = {
            "id": "lib_" + e["id"],
            "category": category_for(e),
            "name": {"en": title(e["name"])},
            "steps": steps,
            "equipment": e.get("equipment"),
            "bodyPart": e.get("body_part"),
            "muscles": [e["target"]] if e.get("target") else [],
            "secondary": e.get("secondary_muscles") or [],
            "credit": HY_CREDIT + ("\n" + EK_CREDIT if k else ""),
        }
        m = motion_for(e["name"])
        if m:
            item["motion"] = m
        if k:
            item["images"] = images(k)
        library.append(item)

    ek_only = []
    for k in ek:
        if k["id"] in matched_ek:
            continue
        item = {
            "id": "ek_" + k["id"],
            "category": "stretching" if "stretch" in k["title"].lower() else "strength",
            "name": {"en": k["title"]},
            "summary": {"en": k.get("primer", "")},
            "steps": {"en": k.get("steps") or []},
            "equipment": ", ".join("body weight" if q == "body" else q for q in k.get("equipment") or []) or "body weight",
            "muscles": list(k["primary"]) if isinstance(k.get("primary"), list) else ([k["primary"]] if k.get("primary") else []),
            "secondary": k.get("secondary") or [],
            "images": images(k),
            "credit": EK_TEXT_CREDIT,
        }
        m = motion_for(k["title"])
        if m:
            item["motion"] = m
        if item["steps"]["en"]:
            ek_only.append(item)

    packs_dir = os.path.join(ROOT, "packs")
    manifest = []

    def add(pid, version, kind, title_, summary, files, license, credit, items):
        rel = f"packs/{pid}/{pid}-{version}.zip"
        size, sha = write_zip(os.path.join(ROOT, rel), files)
        manifest.append({"id": pid, "version": version, "kind": kind, "title": title_, "summary": summary,
                         "file": rel, "size": size, "sha256": sha, "license": license, "credit": credit,
                         "items": items})

    lic_mit = "MIT"
    add("exercise-library", 1, "exercises",
        {"en": "Exercise library", "hi": "व्यायाम लाइब्रेरी"},
        {"en": f"{len(library)} exercises for gym and home: steps in English, Hindi and Spanish, target muscles and equipment.",
         "hi": f"जिम और घर के लिए {len(library)} व्यायाम: अंग्रेज़ी, हिंदी और स्पेनिश में चरण, लक्षित मांसपेशियाँ और उपकरण।"},
        [("pack.json", pack_json("exercise-library", 1, library, [], HY_CREDIT, lic_mit)),
         ("LICENSE.txt", open(os.path.join(ROOT, "licenses", "exercises-dataset-MIT.txt"), encoding="utf-8").read())],
        lic_mit, HY_CREDIT, len(library))

    img_files = []
    for k in ek:
        for pose in ("relaxation", "tension"):
            p = os.path.join(img_dir, f"{k['id']}-{pose}.png")
            if os.path.exists(p):
                img_files.append((f"{k['id']}-{pose}.png", open(p, "rb").read()))
    add("illustrations", 1, "exercises",
        {"en": "Exercise illustrations", "hi": "व्यायाम चित्र"},
        {"en": f"Start and end drawings for {len(ek)} exercises, plus {len(ek_only)} more illustrated exercises.",
         "hi": f"{len(ek)} व्यायामों के शुरुआती और अंतिम चित्र, और {len(ek_only)} और चित्रित व्यायाम।"},
        [("pack.json", pack_json("illustrations", 1, ek_only, [], EK_TEXT_CREDIT, "CC BY-SA 4.0")),
         ("CREDITS.txt", EK_TEXT_CREDIT + "\nLicence: https://creativecommons.org/licenses/by-sa/4.0/\n"
                         "Changes: converted to grayscale, trimmed and resized.\nSource: https://github.com/everkinetic/data\n")]
        + img_files,
        "CC BY-SA 4.0", EK_CREDIT, len(ek))

    for pid, p in authored.PACKS.items():
        add(pid, 1, "exercises", p["title"], p["summary"],
            [("pack.json", pack_json(pid, 1, p["exercises"], p["programs"], "Personality", lic_mit))],
            lic_mit, "Personality", len(p["exercises"]))

    json.dump({"schema": 1, "updated": "2026-10-12", "packs": manifest},
              open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)
    with_motion = sum(1 for e in library if "motion" in e)
    print(f"library {len(library)} (figure {with_motion}, illustrated {len(pairs)}), ek-only {len(ek_only)}")
    for m in manifest:
        print(f"  {m['id']}: {m['size'] // 1024} KB, {m['items']} items")
    return pairs


if __name__ == "__main__":
    pairs = main(*sys.argv[1:4])
    if len(sys.argv) > 4:
        for hid, k in sorted(pairs.items()):
            print(hid, "<-", k["title"])
