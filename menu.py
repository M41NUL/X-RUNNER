# ─────────────────────────────────────────
#  X-RUNNER — menu.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

import os, sys
from config  import LOG_DIR, LANG_MAP
from runner  import run_file, load_last, detect_lang
from utils   import (clear, ok_msg, err_msg, info_msg, warn_msg,
                     separator, prompt, pause, progress_bar,
                     R, G, Y, B, M, C, W, O, PK, LG, BLD, DIM, RST)
from banner  import show_banner

def _menu_header():
    print(f"\n  {O}{BLD}+{'='*44}+{RST}")
    print(f"  {O}{BLD}|{Y}          MAIN MENU  --  X-RUNNER         {O}|{RST}")
    print(f"  {O}{BLD}+{'='*44}+{RST}\n")

def _option(num, label, desc, nc=Y):
    print(f"  {O}{BLD}[{num}]{RST}  {nc}{BLD}{label}{RST}")
    print(f"        {DIM}{W}{desc}{RST}\n")


def show_menu():
    while True:
        clear()
        show_banner()
        _menu_header()

        last = load_last()
        last_name = os.path.basename(last) if last else "None"

        _option("1", "Run File",       "Enter file path and run it")
        _option("2", "Run Last File",  f"Re-run last file  ({last_name})", C)
        _option("3", "View Logs",      "Browse saved run logs")
        _option("4", "Clear Logs",     "Delete all saved logs")
        _option("5", "Supported Langs","Show all supported languages")
        _option("0", "Exit",           "Quit X-RUNNER", R)
        separator()

        choice = prompt("Select option", color=G)

        if   choice == "1": _handle_run()
        elif choice == "2": _handle_run_last()
        elif choice == "3": _handle_view_logs()
        elif choice == "4": _handle_clear_logs()
        elif choice == "5": _handle_langs()
        elif choice == "0": _exit(); break
        else:
            warn_msg("Invalid option.")
            pause()


def _handle_run():
    clear(); show_banner()
    print(f"\n  {G}{BLD}[ RUN FILE ]{RST}\n")
    separator()

    filepath = prompt("Enter file path",
                      example="/sdcard/myproject/main.py")
    if not filepath:
        err_msg("No path entered.")
        pause(); return

    args = prompt("Enter arguments (leave blank if none)",
                  example="--debug arg1 arg2")

    run_file(filepath, args)
    pause()


def _handle_run_last():
    last = load_last()
    if not last:
        err_msg("No last file found. Run a file first.")
        pause(); return

    clear(); show_banner()
    print(f"\n  {C}{BLD}[ RUN LAST FILE ]{RST}\n")
    separator()
    info_msg(f"File: {last}")

    args = prompt("Enter arguments (leave blank if none)",
                  example="--debug arg1")

    run_file(last, args)
    pause()


def _handle_view_logs():
    clear(); show_banner()
    print(f"\n  {Y}{BLD}[ VIEW LOGS ]{RST}\n")
    separator()

    if not os.path.isdir(LOG_DIR):
        warn_msg("No logs found.")
        pause(); return

    logs = sorted([
        f for f in os.listdir(LOG_DIR)
        if f.endswith(".log")
    ], reverse=True)

    if not logs:
        warn_msg("No logs found.")
        pause(); return

    print(f"  {G}{BLD}  Recent logs ({len(logs)} total):{RST}\n")
    for i, log in enumerate(logs[:20], 1):
        size = os.path.getsize(os.path.join(LOG_DIR, log))
        print(f"  {O}{BLD}[{i:2d}]{RST}  {W}{log}{RST}  {DIM}({size}b){RST}")

    separator()
    choice = prompt(f"Select log to view [1-{min(len(logs),20)}] or 0 to go back")
    if choice == "0" or not choice:
        return

    try:
        idx  = int(choice) - 1
        path = os.path.join(LOG_DIR, logs[idx])
        print(f"\n  {Y}{'─'*56}{RST}\n")
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                print(f"  {W}{line}{RST}", end="")
        print(f"\n  {Y}{'─'*56}{RST}")
    except (ValueError, IndexError):
        err_msg("Invalid selection.")

    pause()


def _handle_clear_logs():
    clear(); show_banner()
    print(f"\n  {R}{BLD}[ CLEAR LOGS ]{RST}\n")
    separator()

    if not os.path.isdir(LOG_DIR):
        warn_msg("No logs found.")
        pause(); return

    logs = [f for f in os.listdir(LOG_DIR) if f.endswith(".log")]
    if not logs:
        warn_msg("No logs found.")
        pause(); return

    warn_msg(f"This will delete {len(logs)} log file(s).")
    confirm = prompt("Type YES to confirm")
    if confirm.upper() == "YES":
        progress_bar("Clearing logs", total=20)
        for log in logs:
            try:
                os.remove(os.path.join(LOG_DIR, log))
            except Exception:
                pass
        ok_msg(f"Deleted {len(logs)} log(s).")
    else:
        info_msg("Cancelled.")

    pause()


def _handle_langs():
    clear(); show_banner()
    print(f"\n  {M}{BLD}[ SUPPORTED LANGUAGES ]{RST}\n")
    separator()
    print(f"  {G}{BLD}  {'Ext':<8}{'Language':<14}{'Runner':<12}{'Compiled'}{RST}\n")

    colors = [R, Y, G, C, M, O, PK, LG, B]
    for i, (ext, info) in enumerate(LANG_MAP.items()):
        cc       = colors[i % len(colors)]
        compiled = "Yes" if info.get("compile") else "No"
        print(f"  {cc}{BLD}{ext:<8}{RST}{W}{info['name']:<14}{info['cmd']:<12}{compiled}{RST}")

    print()
    separator()
    pause()


def _exit():
    print(f"\n  {G}{BLD}Goodbye from X-RUNNER!{RST}")
    print(f"  {O}github.com/M41NUL  |  t.me/codexm41nul{RST}\n")
