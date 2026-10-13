# Licences and attribution

Each pack lists its sources in `manifest.json` (`license`, `credit`), and every item that needs attribution carries a `credit` field that the app shows on the exercise page.

| Pack | Source | Licence | Notes |
|---|---|---|---|
| `exercise-library` | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) — names, steps (English, Hindi, Spanish), body part, equipment, muscles | MIT, © 2026 Hasan Emir Yıldırım | **Text only.** That repository's GIFs and thumbnails are © Gym visual and need their own licence, so they are **not** included. The full licence travels inside the pack as `LICENSE.txt`. |
| `illustrations` | [everkinetic/data](https://github.com/everkinetic/data) — start/end drawings and text, from everkinetic.com by Greg Priday | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Changed: converted to grayscale, trimmed and resized to 360 px. This pack (and any adaptation of it) stays CC BY-SA 4.0. `CREDITS.txt` travels inside the pack. |
| `yoga-stretch`, `cardio-hiit`, `martial-arts`, `indian-martial-arts`, `face-jaw-neck` | Written for Personality (`src/authored.py`, `src/skills.py`) | MIT | Movements are drawn live by the app's own figure; no images. |

## Rules for adding content

1. Only content we may redistribute: our own, public domain, or an open licence that allows redistribution (MIT, Unlicense, CC BY, CC BY-SA). Record it here.
2. Keep attribution with every item that needs it.
3. No medical claims. Exercises don't move teeth or reshape bone.

## Rebuilding

```
python -I tools/build_packs.py <exercises-dataset/data/exercises.json> <everkinetic dist/exercises.json> <converted png dir>
```

Illustrations are converted with `dart run tool/convert_illustrations.dart <in> <out> 360` from the Personality app repository. Zips are written with fixed timestamps, so the same inputs give the same SHA-256.
