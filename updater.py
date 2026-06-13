# ─────────────────────────────────────────
#  X-RUNNER — updater.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

import urllib.request, re, os, time
from config import VERSION, GITHUB_RAW
from utils  import spinner, ok_msg, warn_msg, info_msg

FILES = ["main.py","config.py","banner.py","runner.py","menu.py","updater.py","utils.py"]

def _fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"X-RUNNER/updater"})
        with urllib.request.urlopen(req, timeout=8) as r:
            return r.read().decode("utf-8")
    except Exception:
        return None

def _ver_tuple(v):
    try: return tuple(int(x) for x in v.strip().split("."))
    except: return (0,)

def check_and_update():
    spinner("Checking for updates", duration=5)
    raw = _fetch(f"{GITHUB_RAW}/version.txt")
    if not raw:
        warn_msg("Could not reach GitHub. Skipping.")
        return
    remote = raw.strip()
    if _ver_tuple(remote) <= _ver_tuple(VERSION):
        ok_msg(f"Already up to date  (v{VERSION})")
        return
    info_msg(f"Update found: v{VERSION} -> v{remote}")
    base = os.path.dirname(os.path.abspath(__file__))
    failed = []
    for fname in FILES:
        data = _fetch(f"{GITHUB_RAW}/{fname}")
        if data is None:
            failed.append(fname); continue
        try:
            with open(os.path.join(base, fname), "w") as f:
                f.write(data)
        except Exception:
            failed.append(fname)
    if failed:
        warn_msg(f"Some files failed: {', '.join(failed)}")
    else:
        ok_msg(f"Updated to v{remote}!")
    time.sleep(1)
