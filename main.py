#!/usr/bin/env python3
# ─────────────────────────────────────────
#  X-RUNNER — main.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils   import clear, ok_msg, info_msg, separator
from banner  import show_banner
from updater import check_and_update
from menu    import show_menu

O = "\033[38;5;208m"; G = "\033[92m"; W = "\033[97m"; BLD = "\033[1m"; RST = "\033[0m"

def main():
    clear()
    show_banner()
    separator(color=O)
    info_msg("Initializing X-RUNNER...")
    print()
    try:
        check_and_update()
    except (KeyboardInterrupt, Exception):
        pass
    print()
    ok_msg("Ready! Loading main menu...")
    time.sleep(1)
    show_menu()

if __name__ == "__main__":
    main()
