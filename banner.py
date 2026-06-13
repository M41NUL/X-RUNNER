# ─────────────────────────────────────────
#  X-RUNNER — banner.py  (Colorful pixel style)
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

from config import (TOOL_NAME, VERSION, DEV_NAME, DEV_BRAND, DEV_GITHUB,
                    DEV_TELEGRAM, DEV_CHANNEL, DEV_GROUP, DEV_EMAIL,
                    DEV_YOUTUBE, DEV_WHATSAPP, COPYRIGHT)
from utils import R, G, Y, B, M, C, W, O, PK, LG, BLD, DIM, RST

# Colorful pixel-style — each letter different color
PIXEL_ART = [
    f" {R}{BLD}██╗{RST}  {Y}{BLD}██╗{RST}      {G}{BLD}██████╗ {RST} {C}{BLD}██╗   ██╗{RST} {M}{BLD}███╗   ██╗{RST} {PK}{BLD}███╗   ██╗{RST} {O}{BLD}███████╗{RST} {R}{BLD}██████╗{RST} ",
    f" {R}{BLD}╚██╗{RST}{Y}{BLD}██╔╝{RST}      {G}{BLD}██╔══██╗{RST} {C}{BLD}██║   ██║{RST} {M}{BLD}████╗  ██║{RST} {PK}{BLD}████╗  ██║{RST} {O}{BLD}██╔════╝{RST} {R}{BLD}██╔══██╗{RST}",
    f"  {Y}{BLD}╚███╔╝{RST}  {G}{BLD}█████╗{RST} {G}{BLD}██████╔╝{RST} {C}{BLD}██║   ██║{RST} {M}{BLD}██╔██╗ ██║{RST} {PK}{BLD}██╔██╗ ██║{RST} {O}{BLD}█████╗  {RST} {R}{BLD}██████╔╝{RST}",
    f"  {Y}{BLD}██╔██╗{RST}  {G}{BLD}╚════╝{RST} {G}{BLD}██╔══██╗{RST} {C}{BLD}██║   ██║{RST} {M}{BLD}██║╚██╗██║{RST} {PK}{BLD}██║╚██╗██║{RST} {O}{BLD}██╔══╝  {RST} {R}{BLD}██╔══██╗{RST}",
    f" {R}{BLD}██╔╝ ██╗{RST}      {G}{BLD}██║  ██║{RST} {C}{BLD}╚██████╔╝{RST} {M}{BLD}██║ ╚████║{RST} {PK}{BLD}██║ ╚████║{RST} {O}{BLD}███████╗{RST} {R}{BLD}██║  ██║{RST}",
    f" {R}{BLD}╚═╝  ╚═╝{RST}      {G}{BLD}╚═╝  ╚═╝{RST} {C}{BLD} ╚═════╝ {RST} {M}{BLD}╚═╝  ╚═══╝{RST} {PK}{BLD}╚═╝  ╚═══╝{RST} {O}{BLD}╚══════╝{RST} {R}{BLD}╚═╝  ╚═╝{RST}",
]

def show_banner():
    print()
    for line in PIXEL_ART:
        print(line)
    print(f"\n  {DIM}{W}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{RST}")
    print(f"  {W}[ v{VERSION} ]  {Y}Multi-Language Script Runner{RST}  {O}|  CODEX-M41NUL{RST}")
    print()
    _info_box()

def _info_box():
    rows_info = [
        ("Tool",    TOOL_NAME, G),
        ("Version", VERSION,   G),
        ("Dev",     DEV_NAME,  O),
        ("Brand",   DEV_BRAND, O),
    ]
    rows_link = [
        ("GitHub",   DEV_GITHUB,   G),
        ("Telegram", DEV_TELEGRAM, C),
        ("Channel",  DEV_CHANNEL,  C),
        ("Group",    DEV_GROUP,    C),
        ("YouTube",  DEV_YOUTUBE,  R),
        ("WhatsApp", DEV_WHATSAPP, LG),
        ("Email",    DEV_EMAIL,    W),
    ]
    all_rows = rows_info + rows_link
    label_w  = max(len(r[0]) for r in all_rows)
    max_val  = max(len(r[1]) for r in all_rows)
    W_BOX    = max(1 + label_w + 2 + max_val + 1,
                   len(f"{TOOL_NAME}  v{VERSION}  -  Multi-Language Script Runner") + 4)

    def border(l, r):
        return f"  {O}{BLD}{l}{'─'*W_BOX}{r}{RST}"

    def center(text, tc=G):
        vl   = len(text)
        lpad = (W_BOX - vl) // 2
        rpad = W_BOX - vl - lpad
        return f"  {O}{BLD}|{RST}{' '*lpad}{tc}{BLD}{text}{RST}{' '*rpad}{O}{BLD}|{RST}"

    def row(label, value, lc=O):
        lp   = label_w - len(label)
        used = 1 + label_w + 2 + len(value) + 1
        rp   = W_BOX - used
        return (f"  {O}{BLD}|{RST} {lc}{BLD}{label}{RST}{' '*lp}"
                f"  {W}{value}{RST}{' '*max(rp,0)}{O}{BLD}|{RST}")

    title = f"{TOOL_NAME}  v{VERSION}  -  Multi-Language Script Runner"
    print(border("+", "+"))
    print(center(title, Y))
    print(border("+", "+"))
    for l, v, c in rows_info:
        print(row(l, v, c))
    print(border("+", "+"))
    for l, v, c in rows_link:
        print(row(l, v, c))
    print(border("+", "+"))
    print(center(COPYRIGHT, O))
    print(border("+", "+"))
    print()
