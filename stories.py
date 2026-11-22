# news-image-20261122 — story slate.
# 38 stories, 7 regions, 9 fields. Every item verified 22 Nov 2026 ~01:25 UTC
# against a named wire/primary source (see SOURCES below). Items whose event
# fell on Fri 19 / Sat 21 Nov carry that date INSIDE their deck; the barrage
# deck never says "Sunday".
# FREEZE PASS Sun 22 Nov ~20:00 WIB: COP31 BLOCKED (no deal adopted, Kurum
# declares no consensus at closing plenary, first deal-less COP since 2009);
# Las Vegas GP won by Verstappen; India Test Day 4 stumps 720/9 dec, NZ
# 119/2 trail 233; brief 24 displaced by the Banten factory fire (Reuters
# wire snapshot 3 killed / 36 missing). ATP final (Alcaraz v Zverev) STILL
# PENDING — starts 18:00 CET / 00:00 WIB Mon; lead 13 stays a preview.
# Peru quake uses the USGS-REVISED 6.7, never 6.9. Basra fire decks only
# "4 killed" — the injured toll is split 30 vs 35 across wires, so it is
# not banked. Japan live-fire and Prince William cover are Thu 19/20 Nov
# announcements and say so in their decks.

LEADS = [
    # (num, region, field, tag, headline, deck, source, art)
    (1, "World", "Climate", "CLIMATE",
     "COP31 collapses: no deal as EU rejects pact",
     "Kurum declares no consensus; 10-page pact not adopted. First deal-less COP since 2009.",
     "Reuters", "cop"),
    (2, "Middle East", "War", "GULF",
     "Iran strikes US bases in Bahrain",
     "IRGC claims Patriot radars hit; Bahrain: civilian site burned, no dead.",
     "Al Jazeera", "bahrain"),
    (3, "Middle East", "War", "GULF",
     "Two tankers struck off Oman",
     "Hits near Khasab Sat; no casualties. A third tanker was hit Fri.",
     "Reuters", "tanker"),
    (4, "Europe", "War", "UKRAINE",
     "400+ drones, 110 missiles rain on Ukraine",
     "Fri-night barrage: 9 killed, ~30 hurt; 3 Kyiv bridges shut.",
     "Reuters", "barrage"),
    (5, "Europe", "War", "BALTIC",
     "Russian ship Sparta II ablaze off Finland",
     "Hit by two suspected drones Sat; fire burns into the night.",
     "AP", "ship"),
    (6, "Americas", "Disasters", "QUAKE",
     "Quake 6.7 shakes Peru's Andes",
     "Fri 19:09 local; felt in Lima; no casualties reported.",
     "USGS", "quake"),
    (7, "Europe", "War", "UKRAINE",
     "Strike on Kryvyi Rih kills boy, 7, and medic",
     "Fri-night double-tap: 2 killed, 60 hurt; homes, hospital hit.",
     "AP", "city"),
    (8, "Americas", "Justice", "MEXICO",
     "Mexico seizes cartel boss 'El Chapo Isidro'",
     "Captured Fri night in Sinaloa; 11 dead in fighting; $5m reward.",
     "Reuters", "desert"),
    (9, "Middle East", "War", "GAZA",
     "Four killed in Gaza strikes amid ceasefire",
     "Sat: 3 killed in Gaza City, 1 near Jabalia; 14 hurt.",
     "Al Jazeera", "gaza"),
    (10, "Asia", "Politics", "NEPAL",
     "Nepal PM flies to Delhi for first state visit",
     "Balendra Shah arrives Sun for 22-23 Nov talks with Modi.",
     "IANS", "plane"),
    (11, "Europe", "Sport", "RUGBY",
     "England 37-12: record rout of All Blacks",
     "Sat at Twickenham: five tries; biggest-ever margin over NZ.",
     "Reuters", "rugby"),
    (12, "Americas", "Sport", "F1",
     "Verstappen wins Las Vegas GP",
     "Beats Norris by 0.6s; Piastri 3rd. Third Vegas win in four years.",
     "AP", "race"),
    (13, "Europe", "Sport", "TENNIS",
     "ATP final today: Alcaraz v Zverev",
     "Alcaraz beat Shelton Sat; Zverev beat Medvedev. Turin.",
     "Reuters", "tennis"),
]

# (num, region, field, one-line text incl. source in parens).
# One line at 9px in a ~232px column holds ~48 chars; the renderer fails
# loudly if any brief exceeds it, so these are kept short on purpose.
# The fuller facts live in the build note, not on the page.
BRIEFS = [
    (14, "Asia", "Politics", "Hong Kong votes for Election Committee (SCMP)"),
    (15, "World", "Tech", "BepiColombo reaches Mercury orbit Sat (ESA)"),
    (16, "Middle East", "Politics", "Eisenkot invites Likud to talks from Sun (AFP)"),
    (17, "Europe", "Politics", "Denmark expels Russian attache (Reuters)"),
    (18, "Asia", "Politics", "France seeks UN action on Myanmar (AFP)"),
    (19, "Asia", "Economy", "Modi opens 19.7-km Nitish Setu bridge Sat (PTI)"),
    (20, "Asia", "Disasters", "Cyclone Akvan: 14 Ranchi flights off (Jagran)"),
    (21, "World", "Economy", "Bitcoin back above $60,000 (Reuters)"),
    (22, "Americas", "Justice", "Gupta jailed 19 yrs 7 mos, Pannun plot (Reuters)"),
    (23, "Asia", "Politics", "Cricketer Chahal joins BJP's OBC Morcha (ANI)"),
    (24, "Asia", "Disasters", "Factory fire kills 3, 36 missing (Reuters)"),
    (25, "Americas", "War", "US airlines warned; no specific threat (CNN)"),
    (26, "Oceania", "Sport", "India 720/9 dec; NZ 119/2, trail 233 (Cricbuzz)"),
    (27, "Africa", "Politics", "Mogadishu rallies back UAE expulsion Fri (QNC)"),
    (28, "Middle East", "Disasters", "Fire at Basra power plant kills 4 Sat (Reuters)"),
    (29, "Europe", "Sport", "France 45-17 Argentina, reach final (Reuters)"),
    (30, "Middle East", "Society", "Lebanon marks 83 yrs; Aoun: Israel out (Xinhua)"),
    (31, "Oceania", "Society", "Fred Nile, veteran NSW politician, dies 92 (ABC)"),
    (32, "Middle East", "War", "Coalition downs 3 Houthi missiles (Reuters)"),
    (33, "Asia", "Politics", "Japan to train live-fire in India, Thu (PIB)"),
    (34, "Asia", "Economy", "Air India extends Jeddah halt to 24 Nov (ANI)"),
    (35, "Europe", "Society", "William backs 10,000 ranger cover, Thu (ANI)"),
    (36, "Europe", "Sport", "Real Madrid 2-1 Celta; Mbappe miss (Reuters)"),
    (37, "Africa", "Politics", "Aswan Forum on Africa's agency closes (AU)"),
    (38, "Asia", "Politics", "Korea minister quits over exam chaos (BBC)"),
]

REGION_ORDER = ["Europe", "Asia", "Americas", "Middle East", "World",
                "Oceania", "Africa"]

DATE_CHECK = [
    ("Shenzhen Trump-Xi-Putin summit", "Thu 19 Nov"),
    ("ICJ Myanmar / Rohingya verdict", "Thu 19 Nov"),
    ("Estonia border-closure decision", "announced Sun 15 Nov"),
    ("Somalia orders UAE envoy out", "Thu 19 Nov"),
    ("Senate Iran vote; Pete Rose pardon; Anthropic IPO", "Thu 19 Nov"),
    ("GTA VI launch", "Thu 19 Nov"),
]

SOURCES_LINE = ("Sources: Reuters, AP, Al Jazeera, AFP, ANI, IANS, ESA, "
                "SCMP, CNN, QNC, Xinhua, ABC, PIB, PTI, Cricbuzz, BBC, "
                "AU, Jagran, USGS.")
