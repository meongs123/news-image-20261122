# news-image-20261122 — BUILD NOTE (Sun 22 Nov 2026 ~08:25–09:00 WIB)

## Verification (final)

- `entry.png`: 1024×1024 RGB PNG, **181,033 bytes** (≤1 MiB),
  sha256 `ac56a03d25271c2603a67f3b27d4bbdb267dbdf24ad3fc0733156eedef9ce0a8`
  (after fix pass, Sun 22 Nov ~08:40 WIB; pre-fix sha was
  `296678601ff6c3a1424fad8a7655f7b9272e67feb9411aca0530a0461b90e33e`)
- Determinism: `compose.py` run 2× → identical sha256 (also re-verified
  after the art fixes: two consecutive runs identical).
- `main.ts` local run (MAKEFUN_OUTPUT_DIR=/tmp/ni22_main, Node 24):
  exit 0, output sha256 identical to entry.png, guards pass.
- Counts: **38 stories (13 leads + 25 briefs), 7 regions, 9 fields.**
  Regions: Europe 9, Asia 8, Americas 7, Middle East 7, World 3,
  Oceania 2, Africa 2. Fields: War 8, Politics 11, Sport 6, Economy 3,
  Disasters 3, Society 3, Justice 2, Climate 1, Tech 1. Recount from
  `stories.py` matches the printed region bar exactly.
- Story numbers: leads 1–13, briefs 14–38, consecutive, no gaps.
- Loud-failure guards fired during the build and caught real defects:
  lead 4 deck overflow (fixed by geometry, not by truncating), brief 14
  and brief 36 too long for one line (briefs rewritten short).
- Map pins: all 13 snapped to land dots; pairwise disc distance ≥19px
  after the leader-line offset pass (audit script, /tmp — no pair <19px).
- Art bleed audit: every one of the 13 illustrations rendered standalone
  at its real size and checked to paint only inside its box (1px
  tolerance) — **NONE** leaking. This caught 6 real bleeds (ship flames
  drawing over lead 1's deck, city/barrage buildings above their boxes,
  rugby pitch lines crossing the headline, race car above its box,
  tennis ball and quake trace outside their boxes) — all fixed in
  `compose.py`.
- Visual: full page viewed; enlarged crops of the big cards, small cards
  and bottom band viewed. No clipped or overlapping text remains. DATE
  CHECK box holds all 6 exclusions inside its border; MAP KEY complete;
  footer 3 lines inside the page.

## Verify-or-drop pass (all 12 resolved, 0 dropped)

All 12 flagged items verified against a named wire/primary source on
22 Nov ~01:25 UTC:

| # | Item | Verdict |
|---|---|---|
| 16 | Eisenkot invites Likud to coalition talks | VERIFIED — AFP, 21 Nov; talks from Sun |
| 25 | US airlines warned on al-Qaeda threat | VERIFIED — CNN/FBI-DHS-TSA bulletin Thu 19 Nov, reported 20 Nov. CORRECTION (fix pass): the printed brief never said "Thu" or "no specific credible threat"; it now reads "US airlines warned; no specific threat (CNN)" |
| 28 | Basra power-plant fire | VERIFIED — Reuters, 21 Nov, 4 killed; injured split 30 vs 35, NOT banked |
| 29 | France 45-17 Argentina | VERIFIED — Reuters, 21 Nov; reach final vs South Africa 29 Nov |
| 30 | Lebanon 83rd independence | VERIFIED — Xinhua/AFP, 21 Nov; Aoun speech Sat, eve of anniversary |
| 32 | Saudi downs 3 Houthi missiles | VERIFIED — Reuters, 21 Nov; three ballistic missiles, early Sat |
| 33 | Japan live-fire training in India | VERIFIED — PIB joint statement, 19 Nov. CORRECTION (fix pass): the printed brief never said "pact signed Thu"; it now carries the date as "Japan to train live-fire in India, Thu (PIB)" |
| 34 | Air India Jeddah suspension to 24 Nov | VERIFIED — ANI, announced Fri 20 Nov |
| 35 | Prince William ranger cover | VERIFIED — ANI, 20 Nov (announced 19 Nov). CORRECTION (fix pass): the printed brief never said "announced Thu"; it now carries the date as "William backs 10,000 ranger cover, Thu (ANI)" |
| 36 | Real Madrid 2-1 Celta, Mbappe penalty miss | VERIFIED — Reuters, 21 Nov; Espi 85th-min winner |
| 37 | Aswan Forum closes | VERIFIED — AU/UNDP; 6th edition 21–22 Nov, closes Sun |
| 38 | Trump: Iran deal "could last 20 years" | VERIFIED — Fox News Sat 21 Nov via JNS/ANI |

Also re-confirmed at build time: COP31 package unveiled overnight,
objections due 03:00 GMT, approval session 06:00 GMT (Reuters, 22 Nov)
— **no deal approved yet**; Gupta sentenced 235 months = 19 yrs 7 mos
on Fri 20 Nov (Reuters/WSJ); Bitcoin back above $60,000 Sat after a
$55,130 low (Reuters $60,192).

## Deck-subject audit (word-for-word, all 38)

- 1 COP31: package — subject "package", verb "lands"; headline softened
  in fix pass (no deal asserted, dawn vote pending) ✓
- 2 Bahrain: Iran strikes US bases; IRGC claim attributed, Bahrain claim
  attributed ✓
- 3 Oman: two tankers struck; third hit Fri ✓
- 4 Barrage: Fri-night, no "Sunday" in deck ✓
- 5 Sparta II: ship hit by suspected drones, fire burns ✓
- 6 Peru: quake 6.7, Fri local, no casualties ✓
- 7 Kryvyi Rih: strike kills boy + medic; double-tap ✓
- 8 El Chapo Isidro: Mexico seizes boss; captured Fri night ✓
- 9 Gaza: four killed in strikes amid ceasefire ✓
- 10 Nepal: PM flies to Delhi; arrives Sun ✓
- 11 England: 37-12 record rout ✓
- 12 Las Vegas GP: tonight, Verstappen on pole; Antonelli penalty ✓
  (result pending — decked as preview)
- 13 ATP final: today, Alcaraz v Zverev; semis Sat ✓ (result pending)
- 14–38 briefs: each headline's subject matches its story; day-dates now
  carried on the page: 15 Sat, 16 Sun, 19 Sat, 27 Fri, 28 Sat, 33 Thu,
  35 Thu, plus 34 "24 Nov". CORRECTION (fix pass): the pre-fix note
  overclaimed — before this fix only #15 carried "Sat" (#16 "Sun",
  #34 "24 Nov"); the other dates lived in the research note, not on the
  page. No inverted actors.

## Late re-check list (mandatory before final submit)

1. COP31 outcome — approved at 06:00 GMT, blocked, or delayed? Freeze
   the lead deck on the outcome. (Session 13:00 WIB Sunday.)
2. Las Vegas GP winner (race ~04:00 GMT Sunday) and ATP final winner
   (Sunday afternoon Turin) — fill in results, or keep preview wording.
3. India Test score — 629/6 at lunch Day 4 will move; freeze at build
   time (done: 629/6, lead 261).
4. Sunday daytime news sweep (Monday) — any big Sunday-daytime story
   should displace the weakest brief. Do NOT fold in a Monday event.

## FIX PASS — Red Team conditions applied (Sun 22 Nov ~08:40 WIB)

- **F1 (HIGH, softened not frozen):** COP31 headline →
  "COP31: new package lands as dawn vote nears". No deal asserted; deck
  unchanged (objections 03:00 GMT, vote 06:00 GMT Sun). Outcome still
  pending at fix time (vote 13:00 WIB) — the evening freeze pass sets the
  final headline + deck on the actual outcome.
- **F2:** footer line 1 → "Every story here happened, or was first
  reported, on the weekend through Sunday morning, 22 November 2026."
  The "on Sunday 22 November 2026" absolute is gone.
- **F3:** briefs dated — #33 Thu, #35 Thu, #19 Sat, #28 Sat, #27 Fri
  (all ≤48 chars; actual lengths 44/44/47/47/46).
- **F4:** #25 → "US airlines warned; no specific threat (CNN)".
- **F5:** lead 2 art redrawn — quadratic-Bézier curved missile paths
  (no symmetric V), impact burst enlarged (spikes + layered glow),
  skyline raised (~55% of box). Viewed at full size: reads as night sky
  + strikes at a glance.
- **F6:** kicker → "ONE DAY, EVERYWHERE".
- **BUILD-NOTE corrections:** verify-or-drop rows 25/33/35 and the
  dated-briefs audit line corrected (see above); the pre-fix note had
  overclaimed deck wording that was never on the page.
- **India Test re-check (~08:40 WIB):** still 629/6 at lunch Day 4
  (Reuters 00:41 UTC; Cricbuzz lunch break) — no newer score available,
  no change.
- **Sunday daytime sweep (~08:40 WIB, ~01:40 UTC):** no clearly stronger
  Sunday story has landed since the build. Checked: EU–Indonesia trade
  deal is real (Reuters) but signed Sat 21 Nov, before the build — not a
  since-build Sunday story, NOT displaced (flagged for the evening freeze
  pass to consider vs #24); Poland missile landings are the Fri 20 Nov
  barrage, already covered by lead 4; Myanmar 4.1 quake minor; UN
  autonomous-weapons talks + FBI database-hack report weaker/unverified.
  Displacement: none. #24 stays.
- **Re-render verification:** `compose.py` 2× → identical sha256
  `ac56a03d…`; `main.ts` exit 0, output byte-identical; entry.png
  1024×1024 RGB, 181,033 B (≤1 MiB); full page + header / big-card /
  lead-2 / briefs / footer crops viewed — all fixes landed, no
  regressions (38 stories, 7 regions, 9 fields, numbers 1–38, Peru 6.7,
  barrage deck never says "Sunday", no make.fun self-reference,
  no filler).
- **STILL PENDING (evening freeze pass, not this pass):** COP31 final
  outcome (vote 06:00 GMT / 13:00 WIB Sun — approve / block / delay →
  final headline + deck); Las Vegas GP winner (race ~04:00 GMT /
  11:00 WIB); ATP final winner (Sun afternoon Turin). Leads 12/13 stay
  preview until then.

## Authorship note

`compose.py` written fresh in-session in 4 substantive turns (helpers →
illustrations → map → layout/assembler) plus targeted fix edits; no file
copied or cloned from the 19th/20th builds. `main.ts` written in 2
messages (copy program, then the guard revision). `stories.py` written
in-session; the briefs block was re-laid out via a shell heredoc rewrite
during the one-line fit fix, then edited again via the edit tool
(brief 36). `entry.png` is generated by `compose.py`, not copied in.

## FREEZE PASS — evening freeze (Sun 22 Nov ~20:00 WIB)

All four outcomes frozen on verified live sources; no invented results.

- **Lead 1 — COP31 BLOCKED, no deal adopted.** Kurum declared no
  consensus at the closing plenary Sun 22 Nov; Reuters collapse report
  12:09 GMT / 19:09 WIB. 10-page Antalya Pact not adopted, no
  fossil-fuel mention, no $120bn figure. First COP to end deal-less
  since Copenhagen 2009. Headline → "COP31 collapses: no deal as EU
  rejects pact"; deck → "Kurum declares no consensus; 10-page pact not
  adopted. First deal-less COP since 2009." Source stays Reuters.
  Numbers strip: "No deal / COP31 collapses"; sub-headline →
  "COP31 talks collapse, no deal • Tankers struck off Oman • Nepal's PM
  in Delhi" (measured with PIL at SERIF_I(15): **621.19px**, < 1000px —
  full wording kept, no shortening needed).
- **Lead 12 — Las Vegas GP: Max Verstappen WON**, 1:27:39.624; Norris
  2nd +0.639s, Piastri 3rd +1.529s; Verstappen's 3rd Vegas win in 4
  years (Formula1.com / FIA / AP). Headline → "Verstappen wins Las
  Vegas GP"; deck → "Beats Norris by 0.6s; Piastri 3rd. Third Vegas win
  in four years." Source stays AP.
- **Lead 13 — ATP final STILL PENDING.** Alcaraz v Zverev has NOT been
  played; final starts 18:00 CET = 00:00 WIB Mon 23 Nov. Lead 13
  UNCHANGED, stays a preview ("ATP final today: Alcaraz v Zverev").
- **Brief 24 — DISPLACED.** Melania brief replaced by the Sunday-reported
  Indonesia factory fire (Reuters, Sun 22 Nov): fire at PT Fonusa
  Agung Mulia candy factory, Cikande, Serang, Banten; 3 killed, 36
  missing, 15 rescued; search ongoing Sunday. Brief now reads
  "Factory fire kills 3, 36 missing (Reuters)" (Asia / Disasters).
  **Moving-toll caveat:** a later Basarnas/BBC midday update put the
  toll at 6 dead, 33 missing — the toll was still moving at freeze time.
  Frozen on the Reuters wire snapshot (3/36) as written; do NOT use
  6/33 on the page.
- **Brief 26 — India Test, Day 4 STUMPS** (ESPNcricinfo + Cricbuzz):
  India 720/9 declared, lead 352; NZ 119/2, trail by 233. One stale
  outlier said 77/2 — ignored. Brief now reads "India 720/9 dec; NZ
  119/2, trail 233 (Cricbuzz)"; numbers strip "720/9 / India in
  Wellington". Cricbuzz added to SOURCES_LINE.
- **Sunday daytime sweep:** the EU–Indonesia trade deal (verified,
  signed Sat 21 Nov) was NOT used — it predates the build. The only
  displacement is #24 (Banten fire). No other stronger Sunday story
  displaced #38 or #34.
- **Counts after freeze (unchanged totals, shifted mix): 38 stories
  (13 leads + 25 briefs), 7 regions, 9 fields.** Regions: Europe 9,
  Asia 9, Americas 6, Middle East 7, World 3, Oceania 2, Africa 2.
  Fields: War 8, Politics 10, Sport 6, Economy 3, Disasters 4,
  Society 3, Justice 2, Climate 1, Tech 1. Story numbers 1–38
  consecutive (renderer asserts 38/7/9 — passed).
- **Re-render verification:** `compose.py` 2× → byte-identical,
  sha256 `fa7a3bf5eeee25718118dcefb557be33717a4127b8c60342a583d9636351e22c`;
  `entry.png` 1024×1024 RGB, **182,415 bytes** (≤1 MiB).
  `main.ts` local run (MAKEFUN_OUTPUT_DIR=/tmp/ni22_main_freeze, Node
  24.22.1): exit 0, output byte-identical to entry.png (same sha256).
  No render guard fired (no overflow); sub-headline measured 621.19px.
- **Visual check:** full page viewed at full size + enlarged crops of
  header (sub-headline, numbers strip), lead 12 card, and briefs 24/26.
  All changed cards read clean — no clipped or overflowing text. Lead 1
  headline wraps to two lines inside its card; briefs 24 and 26 fit on
  one line each. Footer now lists Cricbuzz among the sources.
- **STILL PENDING after this pass:** ATP final winner only (final
  starts 00:00 WIB Mon 23 Nov — after the freeze; cannot be filled
  tonight). Deadline Tue 24 Nov 07:00 WIB. NOT bundled, kit-checked,
  or submitted — main agent handles that after the user's green light.

## FREEZE PASS FOLLOW-UP — #38 displaced (Sun 22 Nov ~20:10 WIB)

- **Brief 38 — DISPLACED.** South Korea Education Minister Choi
  Kyo-jin offered to resign Sunday 22 Nov over last-minute CSAT
  anti-cheating rule changes; President Lee Jae Myung accepted within
  about an hour. Brief now reads "Korea minister quits over exam
  chaos (BBC)" (Asia / Politics). Sources: BBC (22 Nov 09:20 UTC /
  16:20 WIB) + Korea JoongAng Daily / Aju Press / KBS cross-check.
  Old #38 (Trump Iran-deal quote, JNS) removed.
- **Counts after displacement: 38 stories (13 leads + 25 briefs), 7
  regions, 9 fields.** Regions: Europe 9, Asia 10, Americas 5,
  Middle East 7, World 3, Oceania 2, Africa 2. Fields: War 8,
  Politics 10, Sport 6, Economy 3, Disasters 4, Society 3, Justice 2,
  Climate 1, Tech 1. Story numbers 1–38 consecutive (renderer asserts
  38/7/9 — passed). Nothing else changed: leads 1/12/13, briefs 24/26,
  numbers strip and sub-headline all stay as frozen in ef1ee89.
- **Re-render verification:** `compose.py` 2× → byte-identical, sha256
  `0d7b4445ef07bbc6fbf04a0cf89f8613ae8f4bcfe3b611e010c4f8544c3df526`;
  `entry.png` 1024×1024 RGB, **182,304 bytes** (≤1 MiB). `main.ts`
  local run (MAKEFUN_OUTPUT_DIR=/tmp/ni22_main_freeze2, Node 24):
  exit 0, output byte-identical to entry.png. No render guard fired.
- **Visual check:** full page viewed at full size; brief 38 reads
  clean, no clipped or overflowing text.

## FOOTER SOURCE-LIST FIX — follow-up to freeze (Sun 22 Nov ~20:15 WIB)

- **SOURCES_LINE corrected to match the sources actually cited on the
  page.** Added BBC, AU, Jagran, USGS; dropped stale BCCI, JNS, TOI.
  The 19 cited sources now exactly equal the 19 listed (verified
  programmatically from LEADS + BRIEFS). Measured width of the new
  line at DejaVuSans 9px: **575.3px**, drawn at x=12 — ends at ~587px,
  well inside the 1024px page (no width guard exists in the renderer,
  so the measurement was done before rendering). No story, lead,
  brief, number, or compose.py touched.
- **Re-render verification:** `compose.py` 2× → byte-identical, sha256
  `2cbbf39ea924022ef28334f89e4b0c1f252c9a07a9e456a61421a1023fab3765`;
  `entry.png` 1024×1024 RGB, **182,491 bytes** (≤1 MiB). `main.ts`
  local run (MAKEFUN_OUTPUT_DIR=/tmp/ni22_main_freeze3, Node 24):
  exit 0, output byte-identical to entry.png. Counts re-confirmed
  38/7/9, story numbers 1–38 consecutive. Footer viewed at full size:
  the source line reads complete on one line, no clipping.
