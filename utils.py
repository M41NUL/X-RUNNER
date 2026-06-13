# ─────────────────────────────────────────
#  X-RUNNER — utils.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

import sys, time, os

# Colorful scheme — multi-color
R  = "\033[91m"
G  = "\033[92m"
Y  = "\033[93m"
B  = "\033[94m"
M  = "\033[95m"
C  = "\033[96m"
W  = "\033[97m"
O  = "\033[38;5;208m"
PK = "\033[38;5;213m"
LG = "\033[38;5;119m"
BLD= "\033[1m"
DIM= "\033[2m"
RST= "\033[0m"

def clear():
    os.system("clear")

def ok_msg(msg):
    print(f"{G}{BLD}  + {RST}{W}{msg}{RST}")

def err_msg(msg):
    print(f"{R}{BLD}  x {RST}{W}{msg}{RST}")

def info_msg(msg):
    print(f"{O}{BLD}  > {RST}{W}{msg}{RST}")

def warn_msg(msg):
    print(f"{Y}{BLD}  ! {RST}{W}{msg}{RST}")

def separator(color=O):
    print(f"{color}{'─' * 58}{RST}")

def progress_bar(label, total=30):
    bar_width = 30
    for i in range(total + 1):
        filled = int(bar_width * i / total)
        heavy  = max(filled - 1, 0) * 6 // 10
        med    = max(filled - 1, 0) - heavy
        bar    = "▓" * heavy + "▒" * med + ("▶" if filled > 0 else "") + "░" * (bar_width - filled)
        pct    = int(100 * i / total)
        if pct < 40:   bc = R
        elif pct < 80: bc = Y
        else:           bc = G
        sys.stdout.write(f"\r  {W}{label:<20}{RST}  {bc}{BLD}[{bar}]{RST}  {W}{pct:3d}%{RST}")
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def spinner(label, duration=3):
    frames = ["|", "/", "-", "\\"]
    end_at = time.time() + duration
    i = 0
    try:
        while time.time() < end_at:
            sys.stdout.write(f"\r  {Y}{BLD}{frames[i%4]}{RST}  {W}{label}{RST}  ")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write(f"\r  {G}{BLD}+{RST}  {W}{label} - Done!{RST}      \n")
        sys.stdout.flush()
    except KeyboardInterrupt:
        sys.stdout.write("\n")

def prompt(msg, example=None, color=O):
    if example:
        print(f"\n  {DIM}{W}Example : {example}{RST}")
    return input(f"\n  {color}{BLD}>{RST}  {W}{msg}{RST}  ").strip()

def pause():
    input(f"\n  {O}Press ENTER to continue...{RST}  ")
