#!/usr/bin/env python3
"""news-image-20261122 — Sunday 22 November 2026 front page, drawn in code.

Deterministic: no clock, no randomness, no network. Writes entry.png
(1024x1024, RGB) next to this file. Loud-failure guards: any headline,
deck or brief that would need more lines than its box allows raises
SystemExit instead of silently dropping words (the 20-Nov v2 failure).
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stories import LEADS, BRIEFS, REGION_ORDER, DATE_CHECK, SOURCES_LINE

W, H = 1024, 1024
PAPER = (247, 241, 222)
INK = (26, 26, 26)
NAVY = (24, 42, 78)
RED = (178, 34, 34)
RED_DK = (140, 22, 22)
GOLD = (198, 142, 32)
TEAL = (18, 110, 105)
GREY = (110, 104, 90)
LINE = (180, 170, 145)
CARD = (255, 252, 244)

REGION_COLOURS = {
    "Europe": (24, 42, 78), "Asia": (178, 34, 34), "Americas": (18, 110, 105),
    "Middle East": (198, 142, 32), "World": (90, 60, 130),
    "Oceania": (30, 120, 170), "Africa": (120, 90, 40),
}

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SERIF_I = lambda s: font("DejaVuSerif.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy wrap. Raises if any single word is wider than the box."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if not cur:
                raise SystemExit(
                    f"WORD TOO WIDE for box ({max_w}px): {word!r} in {text!r}")
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, fnt, max_w, max_lines, what):
    """Wrap text; FAIL LOUDLY if it needs more lines than the box allows."""
    lines = wrap(draw, text, fnt, max_w)
    if len(lines) > max_lines:
        raise SystemExit(
            f"OVERFLOW in {what}: {len(lines)} lines > {max_lines}: {text!r}")
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for i, line in enumerate(lines):
        draw.text((x, y + i * leading), line, font=fnt, fill=fill)
    return y + len(lines) * leading


def region_counts():
    counts = {r: 0 for r in REGION_ORDER}
    for item in LEADS + BRIEFS:
        counts[item[1]] += 1
    return counts


def field_counts():
    counts = {}
    for item in LEADS + BRIEFS:
        counts[item[2]] = counts.get(item[2], 0) + 1
    return counts


# ---------------------------------------------------------------- illustrations
# Flat-vector, drawn from simple shapes. Each takes (draw, x, y, w, h) and
# paints only inside that box. All geometry is original to this build.

def art_cop(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 226))
    cx, cy, r = x + w // 2, y + h // 2, min(w, h) // 2 - 8
    for k in range(12):
        import math
        a = math.pi * 2 * k / 12
        d.line([cx + int((r + 2) * math.cos(a)), cy + int((r + 2) * math.sin(a)),
                cx + int((r + 6) * math.cos(a)), cy + int((r + 6) * math.sin(a))],
               fill=GOLD, width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(58, 130, 160))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=2)
    d.ellipse([cx - r, cy - r // 3, cx + r, cy + r // 3], outline=(255, 255, 255), width=2)
    d.line([cx, cy - r, cx, cy + r], fill=(255, 255, 255), width=2)
    d.ellipse([cx - r // 2, cy - r // 2, cx - r // 2 + 12, cy - r // 2 + 12],
              fill=(120, 200, 90))
    d.rectangle([x, y + h - 16, x + w, y + h], fill=NAVY)
    d.text((x + 8, y + h - 15), "ANTALYA", font=SANS_B(9), fill=(255, 255, 255))


def art_bahrain(d, x, y, w, h):
    import math
    d.rectangle([x, y, x + w, y + h], fill=(30, 34, 58))
    for sx, sy in [(x + 14, y + 8), (x + w - 16, y + 6),
                   (x + w // 2 + 30, y + 12), (x + w // 3, y + 5)]:
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    # Raised skyline silhouette: taller buildings fill the lower ~55%.
    for bx in range(x + 6, x + w - 6, 26):
        bh = min(30 + ((bx * 7) % 30), h - 6)
        d.rectangle([bx, y + h - bh, bx + 18, y + h], fill=(70, 80, 120))
    d.polygon([(x + w - 46, y + h), (x + w - 30, y + h - 62),
               (x + w - 14, y + h)], fill=(120, 130, 170))
    ix, iy = x + w // 2, y + h - 30  # impact point, above the skyline base

    def bez(p0, p1, p2, n=24):
        pts = []
        for i in range(n + 1):
            t = i / n
            px = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
            py = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
            pts.append((px, py))
        return pts

    # Curved missile paths arcing down to the impact point (not straight
    # chart lines): left arc sweeps in from the upper left, right arc from
    # the upper right.
    d.line(bez((x + 10, y + 12), (x + w // 4, y + h // 2), (ix, iy)),
           fill=(255, 190, 60), width=3)
    d.line(bez((x + w - 12, y + 8), (x + 3 * w // 4, y + h // 2 - 6),
               (ix + 18, iy - 4)), fill=(255, 120, 60), width=3)
    for px, py in [(x + 10, y + 12), (x + w - 12, y + 8)]:
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(255, 210, 90))
    # Enlarged impact burst: radiating spikes + layered glow.
    for k in range(8):
        a = math.pi * 2 * k / 8
        d.line([ix + int(10 * math.cos(a)), iy + int(10 * math.sin(a)),
                ix + int(20 * math.cos(a)), iy + int(20 * math.sin(a))],
               fill=(255, 160, 60), width=2)
    d.ellipse([ix - 16, iy - 12, ix + 16, iy + 12], fill=(255, 140, 40))
    d.ellipse([ix - 9, iy - 7, ix + 9, iy + 7], fill=(255, 200, 80))
    d.ellipse([ix - 4, iy - 3, ix + 4, iy + 3], fill=(255, 240, 180))


def art_tanker(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(190, 220, 235))
    d.rectangle([x, y, x + w, y + int(h * 0.45)], fill=(245, 240, 220))
    for i in range(4):
        yy = y + int(h * 0.45) + 12 + i * 12
        d.line([x + 6, yy, x + w - 6, yy], fill=(90, 140, 175), width=2)
    d.rectangle([x + 18, y + h - 52, x + w - 18, y + h - 30], fill=(150, 40, 30))
    d.rectangle([x + w - 62, y + h - 78, x + w - 30, y + h - 52], fill=(220, 220, 215))
    d.rectangle([x + w - 58, y + h - 90, x + w - 34, y + h - 78], fill=(90, 110, 130))
    for fx, fy, fr in [(x + 46, y + h - 66, 9), (x + 62, y + h - 72, 7),
                       (x + 78, y + h - 64, 6)]:
        d.ellipse([fx - fr, fy - fr, fx + fr, fy + fr], fill=(255, 150, 40))
    d.polygon([(x + 46, y + h - 76), (x + 52, y + h - 96), (x + 58, y + h - 76)],
              fill=(255, 190, 60))


def art_barrage(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(22, 26, 48))
    for sx in range(x + 10, x + w - 8, 18):
        d.ellipse([sx, y + 4 + (sx % 10), sx + 2, y + 6 + (sx % 10)],
                  fill=(255, 255, 255))
    for bx in range(x + 4, x + w - 4, 30):
        bh = min(14 + ((bx * 11) % 16), h - 4)
        d.rectangle([bx, y + h - bh, min(bx + 22, x + w - 1), y + h],
                    fill=(52, 58, 92))
    for dx, dy in [(x + 20, y + 6), (x + w // 2, y + 4), (x + w - 34, y + 8),
                   (x + w // 3, y + 12)]:
        d.line([dx, dy, dx + 10, dy + 14], fill=(255, 200, 80), width=2)
        d.ellipse([dx + 7, dy + 11, dx + 13, dy + 17], fill=(255, 120, 40))
    d.ellipse([x + w - 30, y + h - 14, x + w - 14, y + h - 2], fill=(255, 90, 40))


def art_ship(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(168, 200, 214))
    for i in range(2):
        yy = y + h - 8 + i * 4
        d.line([x + 4, yy, x + w - 4, yy], fill=(80, 130, 160), width=2)
    d.polygon([(x + 20, y + h - 16), (x + w - 20, y + h - 16),
               (x + w - 34, y + h - 4), (x + 34, y + h - 4)], fill=(90, 90, 96))
    d.rectangle([x + w // 2 - 6, y + 8, x + w // 2 + 6, y + h - 16],
                fill=(200, 200, 195))
    for fx, fy, fr in [(x + w // 2 - 18, y + 12, 6), (x + w // 2 + 2, y + 8, 7),
                       (x + w // 2 + 18, y + 14, 5)]:
        d.ellipse([fx - fr, fy - fr, fx + fr, fy + fr], fill=(255, 140, 30))
    d.polygon([(x + w // 2 - 20, y + 14), (x + w // 2 - 14, y + 2),
               (x + w // 2 - 8, y + 14)], fill=(255, 190, 60))


def art_quake(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 222, 200))
    d.polygon([(x, y + h), (x + w // 4, y + 18), (x + w // 2, y + h)],
              fill=(120, 110, 95))
    d.polygon([(x + w // 3, y + h), (x + 2 * w // 3, y + 8),
               (x + w, y + h)], fill=(95, 88, 74))
    d.polygon([(x + w // 4 - 8, y + 26), (x + w // 4 + 8, y + 26),
               (x + w // 4, y + 14)], fill=(255, 255, 255))
    pts = []
    n = 16
    amp = min(8, h // 4)
    for i in range(n + 1):
        px = x + 6 + i * (w - 12) // n
        py = y + h // 2 + (amp if i % 2 else -amp) * (1 if i % 4 in (1, 2) else 2)
        pts.append((px, py))
    d.line(pts, fill=RED, width=3)
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(70, 64, 52))


def art_city(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 214, 196))
    d.rectangle([x + 10, y + h - 18, x + 44, y + h], fill=(150, 140, 125))
    d.rectangle([x + 52, y + h - 26, x + 88, y + h], fill=(130, 120, 108))
    d.rectangle([x + 96, y + h - 15, x + w - 10, y + h], fill=(160, 150, 135))
    for wx in (x + 18, x + 60, x + 104):
        for wy in (y + h - 14, y + h - 8):
            d.rectangle([wx, wy, wx + 6, wy + 5], fill=(255, 220, 120))
    d.line([x + 8, y + 5, x + w - 8, y + 5], fill=RED, width=2)
    for sx in (x + 20, x + w // 2, x + w - 22):
        d.ellipse([sx - 3, y + 9, sx + 3, y + 15], fill=(255, 120, 40))
    d.polygon([(x + w // 2 - 8, y + 20), (x + w // 2 + 8, y + 20),
               (x + w // 2, y + 11)], fill=(255, 90, 40))


def art_desert(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 214, 160))
    d.ellipse([x + w - 30, y + 8, x + w - 8, y + 30], fill=(255, 200, 90))
    d.polygon([(x, y + h), (x + w // 2, y + h - 26), (x + w, y + h)],
              fill=(205, 170, 110))
    d.rectangle([x + 12, y + h - 12, x + w - 12, y + h - 6], fill=(60, 60, 60))
    for cx in (x + 30, x + 60, x + 90):
        d.ellipse([cx - 4, y + h - 18, cx + 4, y + h - 10], fill=(255, 100, 40))
    d.ellipse([x + w // 2 - 12, y + 12, x + w // 2 + 12, y + 36],
              outline=NAVY, width=3)
    d.text((x + w // 2 - 3, y + 18), "$", font=SANS_B(14), fill=NAVY)


def art_gaza(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(210, 222, 228))
    d.rectangle([x + 8, y + h - 16, x + 40, y + h], fill=(140, 135, 120))
    d.rectangle([x + 48, y + h - 22, x + 82, y + h], fill=(120, 116, 102))
    d.rectangle([x + 90, y + h - 13, x + w - 8, y + h], fill=(150, 145, 130))
    for sx, sy in [(x + 24, y + 10), (x + 58, y + 10), (x + 88, y + 12)]:
        d.ellipse([sx - 7, sy - 3, sx + 7, sy + 7], fill=(150, 150, 148))
        d.ellipse([sx - 4, sy - 8, sx + 5, sy - 1], fill=(170, 170, 168))
    d.ellipse([x + w - 26, y + 8, x + w - 8, y + 26], fill=(255, 255, 255))
    d.line([x + 10, y + h - 8, x + w - 10, y + h - 8], fill=GREY, width=2)


def art_plane(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(196, 222, 240))
    for cx in range(x + 8, x + w - 4, 22):
        d.ellipse([cx, y + 10, cx + 4, y + 14], fill=(255, 255, 255))
    d.polygon([(x + 12, y + h // 2), (x + w - 30, y + h // 2 - 8),
               (x + w - 10, y + h // 2 + 2), (x + w - 30, y + h // 2 + 10)],
              fill=(240, 240, 240))
    d.polygon([(x + w // 2, y + h // 2 - 6), (x + w // 2 + 14, y + h // 2 - 14),
               (x + w // 2 + 22, y + h // 2 - 6)], fill=(200, 40, 40))
    d.polygon([(x + w // 2 - 6, y + h // 2 + 6), (x + w // 2 + 4, y + h // 2 + 14),
               (x + w // 2 + 12, y + h // 2 + 6)], fill=(200, 40, 40))
    d.rectangle([x, y + h - 18, x + w // 2, y + h - 12], fill=(220, 40, 40))
    d.rectangle([x, y + h - 12, x + w // 2, y + h - 6], fill=(20, 60, 140))
    d.rectangle([x + w // 2, y + h - 18, x + w, y + h - 6], fill=(220, 20, 60))


def art_rugby(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(34, 110, 60))
    for i in range(max(1, (h - 12) // 14)):
        yy = y + 6 + i * 14
        d.line([x + 6, yy, x + w - 6, yy], fill=(255, 255, 255), width=1)
    d.line([x + 16, y + 6, x + 16, y + h - 6], fill=(255, 255, 255), width=2)
    d.line([x + w - 16, y + 6, x + w - 16, y + h - 6], fill=(255, 255, 255), width=2)
    d.line([x + 16, y + 6, x + w - 16, y + 6], fill=(255, 255, 255), width=2)
    br = min(14, h // 2 - 4)
    d.ellipse([x + w // 2 - 26, y + h // 2 - br, x + w // 2 + 26, y + h // 2 + br],
              fill=(150, 70, 40))
    d.ellipse([x + w // 2 - 26, y + h // 2 - br, x + w // 2 + 26, y + h // 2 + br],
              outline=(255, 255, 255), width=2)
    d.line([x + w // 2 - 26, y + h // 2, x + w // 2 + 26, y + h // 2],
           fill=(255, 255, 255), width=2)


def art_race(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 36, 52))
    for i in range(6):
        d.rectangle([x + i * 16, y + 2, x + i * 16 + 8, y + 7],
                    fill=(255, 255, 255) if i % 2 == 0 else (20, 20, 20))
        d.rectangle([x + i * 16 + 8, y + 7, x + i * 16 + 16, y + 12],
                    fill=(255, 255, 255) if i % 2 == 0 else (20, 20, 20))
    d.rectangle([x, y + h - 8, x + w, y + h - 2], fill=(70, 70, 78))
    for i in range(8):
        d.rectangle([x + 6 + i * 24, y + h - 6, x + 18 + i * 24, y + h - 4],
                    fill=(255, 220, 60))
    d.polygon([(x + 16, y + 16), (x + 40, y + 16), (x + 46, y + 24),
               (x + 22, y + 24)], fill=(200, 30, 30))
    d.rectangle([x + 46, y + 16, x + w - 24, y + 24], fill=(230, 30, 30))
    d.ellipse([x + 26, y + 22, x + 38, y + 30], fill=(20, 20, 20))
    d.ellipse([x + w - 42, y + 22, x + w - 30, y + 30], fill=(20, 20, 20))
    d.ellipse([x + 29, y + 24, x + 35, y + 28], fill=(180, 180, 180))
    d.ellipse([x + w - 39, y + 24, x + w - 33, y + 28], fill=(180, 180, 180))


def art_tennis(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(58, 120, 180))
    d.rectangle([x + 8, y + 8, x + w - 8, y + h - 8], outline=(255, 255, 255), width=2)
    d.line([x + 8, y + h // 2, x + w - 8, y + h // 2], fill=(255, 255, 255), width=2)
    d.line([x + w // 2, y + 8, x + w // 2, y + h - 8], fill=(255, 255, 255), width=2)
    cx, cy, r = x + w // 2, y + h // 2, min(16, h // 2 - 4)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(200, 230, 60))
    d.arc([cx - r, cy - r, cx + r, cy + r], 300, 60, fill=(255, 255, 255), width=3)
    d.arc([cx - r, cy - r, cx + r, cy + r], 120, 240, fill=(255, 255, 255), width=3)


ART = {"cop": art_cop, "bahrain": art_bahrain, "tanker": art_tanker,
       "barrage": art_barrage, "ship": art_ship, "quake": art_quake,
       "city": art_city, "desert": art_desert, "gaza": art_gaza,
       "plane": art_plane, "rugby": art_rugby, "race": art_race,
       "tennis": art_tennis}


# ---------------------------------------------------------------- world map
# Coarse land grid as column ranges per row (60 cols x 24 rows, equirect
# angles: lon -180..180, lat 75..-55). Built from ranges, not typed art,
# so no row can be miscounted.
LAND_RANGES = {
    0: [(3, 16), (28, 52)], 1: [(2, 17), (27, 55)],
    2: [(3, 18), (26, 56)], 3: [(4, 19), (25, 57)],
    4: [(5, 19), (27, 38), (40, 56)], 5: [(6, 20), (27, 37), (40, 55)],
    6: [(7, 21), (28, 36), (41, 54)],
    7: [(8, 21), (28, 38), (39, 43), (45, 53)],
    8: [(9, 20), (29, 39), (40, 43), (45, 48), (50, 53)],
    9: [(10, 16), (30, 40), (46, 48), (50, 53)],
    10: [(11, 15), (30, 40), (46, 47), (51, 54)],
    11: [(12, 15), (31, 40), (52, 55)], 12: [(13, 17), (31, 40), (52, 56)],
    13: [(13, 18), (32, 39), (53, 57)], 14: [(14, 18), (32, 38), (54, 58)],
    15: [(14, 18), (32, 37), (54, 58)], 16: [(15, 18), (33, 37), (53, 59)],
    17: [(15, 18), (33, 36), (53, 58)], 18: [(15, 17), (33, 36), (54, 58)],
    19: [(16, 17), (34, 35), (55, 58)], 20: [(16, 16), (55, 57), (59, 59)],
    21: [(16, 16), (59, 59)], 22: [(16, 16)], 23: [(16, 16)],
}

# (lead num, lon, lat) — approximate places for the 13 leads.
PINS = {
    1: (32, 37), 2: (50, 26), 3: (57, 26), 4: (31, 50), 5: (24, 60),
    6: (-76, -11), 7: (33, 48), 8: (-108, 25), 9: (34, 31), 10: (77, 28),
    11: (-1, 51), 12: (-115, 36), 13: (7, 45),
}


def map_xy(mx, my, mw, mh, lon, lat):
    fx = (lon + 180.0) / 360.0
    fy = (75.0 - lat) / 130.0
    return mx + fx * mw, my + fy * mh


def land_dots(mx, my, mw, mh):
    dots = []
    for r, ranges in LAND_RANGES.items():
        for c0, c1 in ranges:
            for c in range(c0, c1 + 1):
                dots.append((mx + (c + 0.5) * mw / 60.0,
                             my + (r + 0.5) * mh / 24.0))
    return dots


def nearest_land(dots, px, py):
    best, bd = None, 1e9
    for dx, dy in dots:
        dd = (dx - px) ** 2 + (dy - py) ** 2
        if dd < bd:
            best, bd = (dx, dy), dd
    return best, bd ** 0.5


def paint_map(d, mx, my, mw, mh):
    d.rectangle([mx, my, mx + mw, my + mh], fill=(228, 236, 240))
    d.rectangle([mx, my, mx + mw, my + mh], outline=NAVY, width=2)
    dots = land_dots(mx, my, mw, mh)
    for dx, dy in dots:
        d.ellipse([dx - 1.6, dy - 1.6, dx + 1.6, dy + 1.6], fill=(90, 110, 95))
    placed = {}
    for num, (lon, lat) in PINS.items():
        px, py = map_xy(mx, my, mw, mh, lon, lat)
        (lx, ly), dist = nearest_land(dots, px, py)
        if dist > 14:
            raise SystemExit(f"MAP PIN {num} too far from land: {dist:.1f}px")
        # Gulf / Black Sea pins sit within a few px of each other: if the
        # disc would collide with one already placed, offset it along a
        # search ring and join it to its true spot with a leader line.
        tx, ty = lx, ly
        if any(((lx - ox) ** 2 + (ly - oy) ** 2) ** 0.5 < 19
               for ox, oy in placed.values()):
            found = None
            for radius in (13, 17, 21, 25, 29):
                for k in range(12):
                    import math
                    a = math.pi * 2 * k / 12
                    cx, cy = lx + radius * math.cos(a), ly + radius * math.sin(a)
                    if not (mx + 9 <= cx <= mx + mw - 9 and my + 9 <= cy <= my + mh - 9):
                        continue
                    if all(((cx - ox) ** 2 + (cy - oy) ** 2) ** 0.5 >= 19
                           for ox, oy in placed.values()):
                        found = (cx, cy)
                        break
                if found:
                    break
            if not found:
                raise SystemExit(f"MAP PIN {num}: no free disc spot near land")
            tx, ty = found
            d.line([lx, ly, tx, ty], fill=RED, width=1)
            d.ellipse([lx - 2, ly - 2, lx + 2, ly + 2], fill=RED)
        placed[num] = (tx, ty)
        d.ellipse([tx - 8, ty - 8, tx + 8, ty + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((tx - 3, ty - 6), str(num), font=SANS_B(8), fill=(255, 255, 255))
    return placed


# ---------------------------------------------------------------- page layout
MARGIN = 12
CONTENT_W = W - 2 * MARGIN


def paint_header(d):
    d.rectangle([0, 0, W, 26], fill=NAVY)
    d.text((MARGIN, 5), "ONE DAY, EVERYWHERE", font=SANS_B(13), fill=(255, 255, 255))
    right = "SUNDAY EDITION  •  No. 326"
    d.text((W - MARGIN - d.textlength(right, font=SANS_B(11)), 7), right,
           font=SANS_B(11), fill=(200, 200, 200))
    mast = "Sunday 22 November 2026"
    f = SERIF_B(58)
    d.text(((W - d.textlength(mast, font=f)) / 2, 30), mast, font=f, fill=INK)
    d.line([MARGIN, 94, W - MARGIN, 94], fill=INK, width=2)
    sub = ("COP31 talks collapse, no deal  •  Tankers struck off Oman  •  "
           "Nepal's PM in Delhi")
    f2 = SERIF_I(15)
    d.text(((W - d.textlength(sub, font=f2)) / 2, 100), sub, font=f2, fill=(60, 60, 60))
    strip = "38 STORIES  •  7 REGIONS  •  9 FIELDS  •  13 ILLUSTRATED"
    f3 = SANS_B(14)
    d.text(((W - d.textlength(strip, font=f3)) / 2, 122), strip, font=f3, fill=RED_DK)
    d.line([MARGIN, 142, W - MARGIN, 142], fill=LINE, width=1)


def paint_numbers(d):
    cells = [
        ("~200", "nations at COP31"),
        ("No deal", "COP31 collapses"),
        ("400+ / 110", "drones / missiles"),
        ("6.7", "Peru quake"),
        ("37-12", "England v NZ"),
        ("720/9", "India in Wellington"),
    ]
    y0, y1 = 148, 196
    cw = CONTENT_W / 6.0
    for i, (big, small) in enumerate(cells):
        x = MARGIN + i * cw
        if i:
            d.line([x, y0 + 4, x, y1 - 4], fill=LINE, width=1)
        fb = SANS_B(19)
        d.text((x + (cw - d.textlength(big, font=fb)) / 2, y0 + 2), big,
               font=fb, fill=RED_DK)
        fs = SANS(10)
        d.text((x + (cw - d.textlength(small, font=fs)) / 2, y0 + 27), small,
               font=fs, fill=(70, 70, 70))
    d.line([MARGIN, y1, W - MARGIN, y1], fill=LINE, width=1)


def paint_region_bar(d, counts):
    y0, y1 = 202, 226
    total = sum(counts.values())
    x = MARGIN
    for region in REGION_ORDER:
        n = counts[region]
        seg = CONTENT_W * n / total
        d.rectangle([x, y0, x + seg, y1], fill=REGION_COLOURS[region])
        label = f"{region} {n}"
        f = SANS_B(9)
        tw = d.textlength(label, font=f)
        d.text((x + (seg - tw) / 2, y0 + 7), label, font=f, fill=(255, 255, 255))
        x += seg
    d.rectangle([MARGIN, y0, W - MARGIN, y1], outline=INK, width=1)


def paint_lead_card(d, item, x, y, w, h, big):
    x, y, w, h = int(x), int(y), int(w), int(h)
    num, region, field, tag, headline, deck, source, art = item
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=LINE, width=1)
    art_h = 96 if big else 36
    ART[art](d, x + 1, y + 1, w - 2, art_h)
    tag_f = SANS_B(10 if big else 8)
    tw = d.textlength(tag, font=tag_f)
    d.rectangle([x + 6, y + art_h + 5, x + 10 + tw, y + art_h + 20],
                fill=REGION_COLOURS[region])
    d.text((x + 8, y + art_h + 6), tag, font=tag_f, fill=(255, 255, 255))
    d.ellipse([x + w - 24, y + art_h + 4, x + w - 6, y + art_h + 22], fill=RED)
    d.text((x + w - 19, y + art_h + 7), str(num), font=SANS_B(10),
           fill=(255, 255, 255))
    hy = y + art_h + 24
    hf = SERIF_B(19 if big else 13)
    hl = fit(d, headline, hf, w - 12, 2, f"lead {num} headline")
    lead = 21 if big else 14
    draw_lines(d, hl, x + 6, hy, hf, INK, lead)
    dy = hy + len(hl) * lead + 1
    df = SANS(11 if big else 9)
    dl = fit(d, deck, df, w - 12, 2, f"lead {num} deck")
    dlead = 11 if big else 11
    draw_lines(d, dl, x + 6, dy, df, (60, 60, 60), dlead)
    if dy + len(dl) * dlead > y + h - 13:
        raise SystemExit(f"OVERFLOW in lead {num}: deck runs into source line")
    sf = SANS(8 if big else 7)
    d.text((x + 6, y + h - 11), source.upper(), font=sf, fill=GREY)


def paint_leads(d):
    y0 = 232
    big_w, big_h = 322, 200
    gap = (CONTENT_W - 3 * big_w) / 2.0
    for i, item in enumerate(LEADS[:3]):
        paint_lead_card(d, item, MARGIN + i * (big_w + gap), y0, big_w, big_h, True)
    small_w, small_h = 192, 128
    sgap = (CONTENT_W - 5 * small_w) / 4.0
    for row in range(2):
        for col in range(5):
            item = LEADS[3 + row * 5 + col]
            paint_lead_card(d, item, MARGIN + col * (small_w + sgap),
                            y0 + big_h + 8 + row * (small_h + 8),
                            small_w, small_h, False)


def paint_briefs(d, bx, by, bw, bh):
    d.text((bx, by), "ALSO ON THIS PAGE", font=SANS_B(12), fill=NAVY)
    d.line([bx, by + 16, bx + bw, by + 16], fill=NAVY, width=2)
    col_w = (bw - 14) / 2.0
    per_col = 13
    bf = SANS_B(9)
    df = SANS(9)
    row_h = 12.5
    for idx, item in enumerate(BRIEFS):
        num, region, field, text = item
        col = idx // per_col
        row = idx % per_col
        x = bx + col * (col_w + 14)
        y = by + 20 + row * row_h
        if y + 11 > by + bh:
            raise SystemExit(f"BRIEFS overflow at item {num}")
        d.text((x, y), f"{num}.", font=SANS_B(9), fill=RED_DK)
        lines = fit(d, text, df, col_w - 18, 1, f"brief {num}")
        d.text((x + 18, y), lines[0], font=df, fill=INK)


def paint_date_check(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], outline=RED, width=2)
    d.text((x + 8, y + 4), "DATE CHECK — LEFT OUT ON PURPOSE",
           font=SANS_B(11), fill=RED_DK)
    f = SANS(10)
    yy = y + 21
    for name, when in DATE_CHECK:
        d.text((x + 8, yy), f"✕  {name} — {when}", font=f, fill=INK)
        yy += 12


def paint_footer(d, y):
    d.line([MARGIN, y, W - MARGIN, y], fill=LINE, width=1)
    d.text((MARGIN, y + 4),
           "Every story here happened, or was first reported, on the weekend "
           "through Sunday morning, 22 November 2026.",
           font=SANS(10), fill=INK)
    d.text((MARGIN, y + 17), SOURCES_LINE, font=SANS(9), fill=(70, 70, 70))
    d.text((MARGIN, y + 29),
           "Original drawings — no photographs. Pictures and map drawn in code.",
           font=SANS_B(9), fill=(70, 70, 70))


def build():
    counts = region_counts()
    fields = field_counts()
    assert sum(counts.values()) == 38, counts
    assert len(counts) == 7 and len(fields) == 9, (counts, fields)
    assert len(LEADS) == 13 and len(BRIEFS) == 25
    assert [i[0] for i in LEADS] == list(range(1, 14))
    assert [i[0] for i in BRIEFS] == list(range(14, 39))
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    paint_header(d)
    paint_numbers(d)
    paint_region_bar(d, counts)
    paint_leads(d)
    # Bottom band: map left, briefs right.
    by = 706
    d.text((MARGIN, by - 2), "WHERE IT HAPPENED", font=SANS_B(12), fill=NAVY)
    d.line([MARGIN, by + 14, MARGIN + 470, by + 14], fill=NAVY, width=2)
    paint_map(d, MARGIN, by + 20, 470, 138)
    paint_briefs(d, MARGIN + 486, by - 2, CONTENT_W - 486, 190)
    paint_date_check(d, MARGIN, 884, 470, 92)
    # Map legend, right of the DATE CHECK box.
    lx = MARGIN + 486
    d.text((lx, 884), "MAP KEY", font=SANS_B(11), fill=NAVY)
    places = {1: "Antalya (COP31)", 2: "Bahrain", 3: "Strait of Hormuz",
              4: "Kyiv", 5: "Gulf of Finland", 6: "Junin, Peru",
              7: "Kryvyi Rih", 8: "Sinaloa", 9: "Gaza City",
              10: "New Delhi", 11: "Twickenham", 12: "Las Vegas",
              13: "Turin"}
    f = SANS(10)
    for i, n in enumerate(sorted(places)):
        col = i // 7
        row = i % 7
        d.text((lx + col * 250, 900 + row * 11), f"{n}. {places[n]}",
               font=f, fill=INK)
    paint_footer(d, 982)
    return img


def main():
    img = build()
    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
