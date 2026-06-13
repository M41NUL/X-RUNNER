<div align="center">

```
 ██╗  ██╗      ██████╗  ██╗   ██╗ ███╗   ██╗ ███╗   ██╗ ███████╗ ██████╗
 ╚██╗██╔╝      ██╔══██╗ ██║   ██║ ████╗  ██║ ████╗  ██║ ██╔════╝ ██╔══██╗
  ╚███╔╝ █████╗██████╔╝ ██║   ██║ ██╔██╗ ██║ ██╔██╗ ██║ █████╗   ██████╔╝
  ██╔██╗ ╚════╝██╔══██╗ ██║   ██║ ██║╚██╗██║ ██║╚██╗██║ ██╔══╝   ██╔══██╗
 ██╔╝ ██╗      ██║  ██║ ╚██████╔╝ ██║ ╚████║ ██║ ╚████║ ███████╗ ██║  ██║
 ╚═╝  ╚═╝      ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚═══╝ ╚═╝  ╚═══╝ ╚══════╝ ╚═╝  ╚═╝
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  [ v1.0.0 ]  Multi-Language Script Runner  |  CODEX-M41NUL
```

**Multi-Language Script Runner for Termux**

[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen?style=flat-square)](https://github.com/M41NUL/X-RUNNER)
[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Android-orange?style=flat-square)](https://github.com/M41NUL/X-RUNNER)
[![Language](https://img.shields.io/badge/language-Python%20%2B%20Shell-blue?style=flat-square)](https://github.com/M41NUL/X-RUNNER)
[![License](https://img.shields.io/badge/license-MIT-red?style=flat-square)](https://github.com/M41NUL/X-RUNNER)
[![Author](https://img.shields.io/badge/dev-CODEX--M41NUL-yellow?style=flat-square)](https://github.com/M41NUL)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-2CA5E0?style=flat-square&logo=telegram)](https://t.me/codexm41nul)
[![Stars](https://img.shields.io/github/stars/M41NUL/X-RUNNER?style=flat-square&color=yellow)](https://github.com/M41NUL/X-RUNNER/stargazers)
[![Forks](https://img.shields.io/github/forks/M41NUL/X-RUNNER?style=flat-square&color=blue)](https://github.com/M41NUL/X-RUNNER/network/members)
[![Issues](https://img.shields.io/github/issues/M41NUL/X-RUNNER?style=flat-square&color=red)](https://github.com/M41NUL/X-RUNNER/issues)
[![Last Commit](https://img.shields.io/github/last-commit/M41NUL/X-RUNNER?style=flat-square&color=brightgreen)](https://github.com/M41NUL/X-RUNNER/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/M41NUL/X-RUNNER?style=flat-square&color=orange)](https://github.com/M41NUL/X-RUNNER)

</div>

---

## What is X-RUNNER?

**X-RUNNER** is a Termux-based multi-language script runner. Select any file, and X-RUNNER automatically detects the language, runs it with the correct interpreter, streams live output, highlights errors in red, measures run time, and saves a log — all from one interactive menu.

> Run any script from your Android terminal without typing interpreter commands manually.

---

## Features

- Run Python, JavaScript, Shell, PHP, Ruby, Perl, Lua, R scripts directly
- Compile and run C, C++, Java automatically
- Auto-detect language from file extension
- Live output streaming — see results as they happen
- Error output highlighted in red, separate from normal output
- Run time display — shows how long execution took
- Pass arguments to your scripts
- Remember last file — re-run with one keypress
- Save run logs to /sdcard/X-RUNNER/logs/
- View and clear logs from the menu
- Auto update check from GitHub on every launch
- Smart installer — skips already installed packages
- Colorful pixel-style banner (each letter different color)

---

## Project Structure

```
X-RUNNER/
├── main.py        - Entry point (banner, update check, menu)
├── config.py      - Config, language map, developer info
├── banner.py      - Colorful pixel-style ASCII banner
├── runner.py      - Core run logic (live output, compile, log)
├── menu.py        - Interactive menu and input handlers
├── updater.py     - Auto update from GitHub
├── utils.py       - Colors, progress bar, prompts
├── installer.sh   - Smart installer + launcher
└── version.txt    - Version tracking
```

---

## Installation

### Step 1 - Clone the repo

```bash
git clone https://github.com/M41NUL/X-RUNNER.git
cd X-RUNNER
```

### Step 2 - Run installer

```bash
bash installer.sh
```

The installer will:
- Update Termux packages
- Install Python, pip, git, nodejs
- Skip already installed packages
- Request Android storage permission (once only)
- Auto-launch main.py after a 3-second countdown

### Step 3 - Run manually (after first install)

```bash
cd X-RUNNER
python main.py
```

---

## All Commands

| Command | Description |
|---------|-------------|
| `git clone https://github.com/M41NUL/X-RUNNER.git` | Clone the repo |
| `cd X-RUNNER` | Enter project folder |
| `bash installer.sh` | Install and launch |
| `python main.py` | Run manually |
| `git pull origin main` | Pull latest update manually |
| `rm -rf X-RUNNER` | Remove / uninstall |

---

## Uninstall

```bash
cd /sdcard
rm -rf X-RUNNER
rm -f ~/.xrunner_last
```

---

## Menu Options

```
[1]  Run File         - Enter file path and run it
[2]  Run Last File    - Re-run the last executed file
[3]  View Logs        - Browse and read saved run logs
[4]  Clear Logs       - Delete all saved logs
[5]  Supported Langs  - Show all supported languages
[0]  Exit
```

---

## Supported Languages

| Extension | Language   | Runner   | Compiled |
|-----------|-----------|----------|----------|
| `.py`     | Python     | python   | No       |
| `.js`     | JavaScript | node     | No       |
| `.sh`     | Shell      | bash     | No       |
| `.php`    | PHP        | php      | No       |
| `.rb`     | Ruby       | ruby     | No       |
| `.pl`     | Perl       | perl     | No       |
| `.lua`    | Lua        | lua      | No       |
| `.r`      | R          | Rscript  | No       |
| `.c`      | C          | gcc      | Yes      |
| `.cpp`    | C++        | g++      | Yes      |
| `.java`   | Java       | javac    | Yes      |

---

## Run File Example

```
Enter file path            : /sdcard/myproject/main.py
Enter arguments (optional) : --debug arg1
```

```
> File     : main.py
> Language : Python
> Size     : 1.2KB  |  Lines: 48
> Runner   : python
> Args     : --debug arg1

  ────────────────────────────────────────────────────
  Running...  python main.py

  Hello from X-RUNNER!
  Debug mode enabled.

  ────────────────────────────────────────────────────
  + Finished in 0.43s  |  Exit: 0
  + Log saved : /sdcard/X-RUNNER/logs/20260613_main.py.log
```

---

## Run with Arguments Example

```
Enter file path            : /sdcard/bot/bot.py
Enter arguments (optional) : --token abc123 --debug
```

Internally runs:
```bash
python /sdcard/bot/bot.py --token abc123 --debug
```

---

## Log File Format

Every run saves a log to `/sdcard/X-RUNNER/logs/`:

```
X-RUNNER Log
==================================================
File     : /sdcard/myproject/main.py
Args     : --debug
Date     : 2026-06-13 09:00:00
Duration : 0.43s
Exit     : 0
==================================================

OUTPUT:
Hello from X-RUNNER!
Debug mode enabled.
```

---

## Developer

<div align="center">

| | |
|--|--|
| **Name** | Md. Mainul Islam |
| **Brand** | CODEX-M41NUL |
| **GitHub** | [github.com/M41NUL](https://github.com/M41NUL) |
| **Telegram** | [t.me/mdmainulislaminfo](https://t.me/mdmainulislaminfo) |
| **Channel** | [t.me/codexm41nul](https://t.me/codexm41nul) |
| **Group** | [t.me/codex_m41nul](https://t.me/codex_m41nul) |
| **YouTube** | [youtube.com/@codexm41nul](https://youtube.com/@codexm41nul) |
| **WhatsApp** | +8801308850528 |
| **Email** | devmainulislam@gmail.com |

</div>

---

## Support

[![Star on GitHub](https://img.shields.io/github/stars/M41NUL/X-RUNNER?style=social)](https://github.com/M41NUL/X-RUNNER)
[![Telegram](https://img.shields.io/badge/Join-Telegram%20Channel-2CA5E0?style=flat-square&logo=telegram)](https://t.me/codexm41nul)

---

<div align="center">
<sub>© 2026 CODEX-M41NUL. All Rights Reserved.</sub>
</div>
