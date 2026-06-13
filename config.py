# ─────────────────────────────────────────
#  X-RUNNER — config.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

from datetime import datetime
import os

TOOL_NAME    = "X-RUNNER"
VERSION      = "1.0.0"
GITHUB_USER  = "M41NUL"
GITHUB_REPO  = "X-RUNNER"

GITHUB_RAW   = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main"
VERSION_URL  = f"{GITHUB_RAW}/version.txt"

DEV_NAME     = "Md. Mainul Islam"
DEV_BRAND    = "CODEX-M41NUL"
DEV_GITHUB   = "github.com/M41NUL"
DEV_TELEGRAM = "t.me/mdmainulislaminfo"
DEV_CHANNEL  = "t.me/codexm41nul"
DEV_GROUP    = "t.me/codex_m41nul"
DEV_EMAIL    = "devmainulislam@gmail.com"
DEV_YOUTUBE  = "youtube.com/@codexm41nul"
DEV_WHATSAPP = "+8801308850528"

YEAR         = datetime.now().year
COPYRIGHT    = f"© {YEAR} CODEX-M41NUL. All Rights Reserved."

LOG_DIR      = "/sdcard/X-RUNNER/logs"
LAST_FILE    = os.path.expanduser("~/.xrunner_last")

# Language → interpreter mapping
LANG_MAP = {
    ".py":   {"name": "Python",     "cmd": "python",   "install": "python"},
    ".js":   {"name": "JavaScript", "cmd": "node",     "install": "nodejs"},
    ".sh":   {"name": "Shell",      "cmd": "bash",     "install": "bash"},
    ".php":  {"name": "PHP",        "cmd": "php",      "install": "php"},
    ".rb":   {"name": "Ruby",       "cmd": "ruby",     "install": "ruby"},
    ".pl":   {"name": "Perl",       "cmd": "perl",     "install": "perl"},
    ".lua":  {"name": "Lua",        "cmd": "lua",      "install": "lua54"},
    ".r":    {"name": "R",          "cmd": "Rscript",  "install": "r-base"},
    ".c":    {"name": "C",          "cmd": "gcc",      "install": "clang", "compile": True},
    ".cpp":  {"name": "C++",        "cmd": "g++",      "install": "clang", "compile": True},
    ".java": {"name": "Java",       "cmd": "javac",    "install": "openjdk-17", "compile": True},
}
