# news-image-20261122 — Sunday 22 November 2026 in one image

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/meongs123/news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/meongs123/news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A make.fun bounty entry: a newspaper front page summing up the world's news
of **Sunday 22 November 2026** — 38 stories, 7 regions, 9 fields, 13 drawn
illustrations, a dotted world map with numbered pins, one-line briefs, and a
DATE CHECK box naming the stories left out on purpose.

## The image

- Masthead: **Sunday 22 November 2026**, with the count strip
  (38 stories · 7 regions · 9 fields · 13 illustrated), a numbers strip
  (~200 nations at COP31, 03:00 GMT objection deadline, 400+ drones /
  110 missiles, 6.7 Peru quake, 37–12 England, 629/6 India) and a
  segmented region bar.
- Lead story: **COP31** — the new package unveiled overnight, objections due
  03:00 GMT, approval vote 06:00 GMT Sunday. No approval is claimed: at
  build time (01:25 UTC) the vote had not happened yet.
- 3 big + 10 small illustrated lead cards, a dotted world map with 13
  numbered pins, 25 numbered one-line briefs, and a red-bordered DATE CHECK
  box (Shenzhen summit, ICJ Myanmar verdict, Estonia border decision,
  Somalia–UAE order, Senate Iran vote / Pete Rose pardon / Anthropic IPO,
  GTA VI launch — all 19 Nov or earlier).
- Every picture is an original flat-vector drawing made in code. No
  photographs. Sources are tagged per story.

## Facts, frozen at build time (Sun 22 Nov ~01:25 UTC)

- Peru quake uses the USGS-**revised 6.7** (not the first 6.9).
- The 400-drone barrage is the **Friday-night** 19→20 Nov attack; its deck
  never says "Sunday".
- Basra power-plant fire decks only "4 killed" — wires split 30 vs 35
  injured, so no injured figure is banked.
- Friday/Saturday items (barrage, quake, Kryvyi Rih, El Chapo Isidro
  capture, BepiColombo, Japan live-fire pact, Prince William cover, US
  airline warning, Gupta sentence) are dated inside their decks.
- **Still pending at build time — late re-check before submit:** the COP31
  approval vote (06:00 GMT), the Las Vegas GP result (race ~04:00 GMT)
  and the ATP final result (Sunday afternoon, Turin). This build decks
  all three honestly as pending/preview.

## Files

- `main.ts` — the entrypoint (Node 22, stdlib only): copies `entry.png`
  to `/output/entry.png` and guards the PNG signature, the 1 MiB cap,
  the 1024×1024 size, and a byte-identical round trip.
- `entry.png` — the image (1024×1024, 179,810 bytes), drawn by `compose.py`.
- `compose.py` — the deterministic renderer (PIL, no clock, no randomness,
  no network). It fails loudly instead of truncating: any headline, deck
  or brief that needs more lines than its box allows raises, and every
  illustration is audited to paint only inside its own box.
- `stories.py` — the 38-story slate with regions, fields and sources.
- `BUILD-NOTE.md` — the full verification record and source list.

## Verify locally

```sh
python3 compose.py            # regenerates entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE` (SPDX: MIT).
