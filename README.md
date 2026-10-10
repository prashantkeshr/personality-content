# Personality — content packs

Optional content for the [Personality](https://github.com/prashantkeshr/personality) app, downloaded **only when the user asks for it**.

- **No user data ever comes here.** The app only downloads files from this repository; it never uploads anything.
- Packs are small, versioned and verified: the app checks every file's SHA-256 against `manifest.json` before using it.
- Once downloaded, a pack works fully offline. Users can remove packs at any time.

## Layout

```
manifest.json          index of packs (id, version, size, sha256, licence, credits)
packs/<pack-id>/       pack sources (JSON + media), published as release assets
LICENSES.md            licence of every source used, with attribution rules
```

## Packs (planned)

| Pack | Contents |
|---|---|
| `strength` | Strength and mobility exercises: steps, muscles, equipment, levels |
| `yoga-stretch` | Yoga poses and stretching routines |
| `cardio-hiit` | Cardio and HIIT drills |
| `martial-arts` | Solo drills: karate, kung fu, boxing and kickboxing (no sparring) |
| `face-jaw-neck` | Jaw relaxation, neck posture and face routines, with realistic expectations |

## Rules for adding content

1. Only content we may redistribute: our own, public domain, or an open licence that allows redistribution (e.g. CC BY / CC BY-SA, MIT, Unlicense). Record it in `LICENSES.md`.
2. Keep attribution with every item that needs it (`credit` field).
3. No medical claims. Exercises don't move teeth or reshape bone.
