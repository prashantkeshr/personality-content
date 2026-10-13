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

## Packs

| Pack | Contents | Size |
|---|---|---|
| `exercise-library` | 1,324 gym and home exercises: steps in English, Hindi and Spanish, muscles, equipment | ~0.4 MB |
| `illustrations` | Start/end line drawings for 269 exercises (139 matched to the library, 130 extra) | ~8.6 MB |
| `yoga-stretch` | 16 yoga poses and stretches, 3 guided routines | ~5 KB |
| `cardio-hiit` | 9 no-equipment cardio moves, HIIT 12, low-impact and Tabata routines | ~3 KB |
| `martial-arts` | 20 solo boxing, Muay Thai, karate, kung fu and self-defence techniques, 5 routines (no sparring) | ~6 KB |
| `indian-martial-arts` | 22 techniques from Kalaripayattu, Silambam, Gatka, Mardani Khel, Thang-ta, Kushti, Musti Yuddha and Lathi Khela, 4 routines | ~6 KB |
| `face-jaw-neck` | 13 jaw, tongue-posture, neck and face exercises, 3 routines, with honest expectations | ~4 KB |

Sizes and checksums are in `manifest.json`. See `LICENSES.md` for sources.

## Rules for adding content

1. Only content we may redistribute: our own, public domain, or an open licence that allows redistribution (e.g. CC BY / CC BY-SA, MIT, Unlicense). Record it in `LICENSES.md`.
2. Keep attribution with every item that needs it (`credit` field).
3. No medical claims. Exercises don't move teeth or reshape bone.
