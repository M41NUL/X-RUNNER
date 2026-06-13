# ─────────────────────────────────────────
#  X-RUNNER — runner.py
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

import os, sys, subprocess, time, shutil, tempfile
from datetime import datetime
from config import LANG_MAP, LOG_DIR, LAST_FILE
from utils  import ok_msg, err_msg, info_msg, warn_msg, separator, R, G, Y, C, W, O, M, BLD, DIM, RST


def detect_lang(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    return LANG_MAP.get(ext)


def get_file_info(filepath):
    size  = os.path.getsize(filepath)
    lines = 0
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = sum(1 for _ in f)
    except Exception:
        pass
    return size, lines


def check_interpreter(cmd):
    return shutil.which(cmd) is not None


def save_last(filepath):
    try:
        with open(LAST_FILE, "w") as f:
            f.write(filepath)
    except Exception:
        pass


def load_last():
    try:
        if os.path.exists(LAST_FILE):
            with open(LAST_FILE) as f:
                return f.read().strip()
    except Exception:
        pass
    return None


def save_log(filepath, args, output, errors, duration, exit_code):
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        ts       = datetime.now().strftime("%Y%m%d_%H%M%S")
        fname    = os.path.basename(filepath)
        log_path = os.path.join(LOG_DIR, f"{ts}_{fname}.log")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"X-RUNNER Log\n")
            f.write(f"{'='*50}\n")
            f.write(f"File     : {filepath}\n")
            f.write(f"Args     : {args}\n")
            f.write(f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Duration : {duration:.2f}s\n")
            f.write(f"Exit     : {exit_code}\n")
            f.write(f"{'='*50}\n\n")
            f.write("OUTPUT:\n")
            f.write(output or "(no output)\n")
            if errors:
                f.write("\nERRORS:\n")
                f.write(errors)
        return log_path
    except Exception as e:
        return None


def run_compiled(filepath, lang_info, args):
    """Handle C, C++, Java — compile then run."""
    ext      = os.path.splitext(filepath)[1].lower()
    base     = os.path.splitext(filepath)[0]
    tmp_dir  = tempfile.mkdtemp(prefix="xrunner_")

    try:
        if ext in (".c", ".cpp"):
            compiler  = "gcc" if ext == ".c" else "g++"
            out_bin   = os.path.join(tmp_dir, "a.out")
            compile_cmd = [compiler, filepath, "-o", out_bin]

            info_msg(f"Compiling with {compiler}...")
            cr = subprocess.run(compile_cmd, capture_output=True, text=True)
            if cr.returncode != 0:
                print(f"\n{R}{BLD}  Compile Error:{RST}")
                print(cr.stderr)
                return None, cr.stderr, 1

            ok_msg("Compiled successfully.")
            run_cmd = [out_bin] + (args.split() if args else [])

        elif ext == ".java":
            compile_cmd = ["javac", "-d", tmp_dir, filepath]
            info_msg("Compiling Java...")
            cr = subprocess.run(compile_cmd, capture_output=True, text=True)
            if cr.returncode != 0:
                print(f"\n{R}{BLD}  Compile Error:{RST}")
                print(cr.stderr)
                return None, cr.stderr, 1

            ok_msg("Compiled successfully.")
            class_name = os.path.splitext(os.path.basename(filepath))[0]
            run_cmd = ["java", "-cp", tmp_dir, class_name] + (args.split() if args else [])

        return _execute(run_cmd, filepath)

    finally:
        import shutil as sh
        sh.rmtree(tmp_dir, ignore_errors=True)


def _execute(cmd, filepath):
    """Run a command, stream output live, return (output, errors, exit_code)."""
    print(f"\n  {Y}{'─'*56}{RST}")
    print(f"  {G}{BLD}Running...{RST}  {DIM}{W}{' '.join(cmd[:3])}{RST}")
    print(f"  {Y}{'─'*56}{RST}\n")

    output_lines = []
    error_lines  = []
    start        = time.time()

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        # Stream stdout live
        for line in proc.stdout:
            sys.stdout.write(f"  {W}{line}{RST}")
            sys.stdout.flush()
            output_lines.append(line)

        proc.wait()

        # Collect stderr
        for line in proc.stderr:
            error_lines.append(line)

        duration  = time.time() - start
        exit_code = proc.returncode

        print(f"\n  {Y}{'─'*56}{RST}")
        if exit_code == 0:
            print(f"  {G}{BLD}+ Finished in {duration:.2f}s  |  Exit: {exit_code}{RST}")
        else:
            print(f"  {R}{BLD}x Finished in {duration:.2f}s  |  Exit: {exit_code}{RST}")

        if error_lines:
            print(f"\n  {R}{BLD}Errors:{RST}")
            for line in error_lines:
                print(f"  {R}{line}{RST}", end="")

        print(f"  {Y}{'─'*56}{RST}")

        return "".join(output_lines), "".join(error_lines), exit_code, duration

    except FileNotFoundError:
        duration = time.time() - start
        err_msg(f"Command not found: {cmd[0]}")
        return "", f"Command not found: {cmd[0]}", 127, duration
    except KeyboardInterrupt:
        duration = time.time() - start
        print(f"\n\n  {Y}{BLD}! Interrupted by user.{RST}")
        proc.terminate()
        return "".join(output_lines), "Interrupted", 130, duration


def run_file(filepath, args=""):
    """Main run function."""
    filepath = os.path.expandvars(os.path.expanduser(filepath.strip()))

    if not os.path.isfile(filepath):
        err_msg(f"File not found: {filepath}")
        return

    lang_info = detect_lang(filepath)
    if not lang_info:
        err_msg(f"Unsupported file type: {os.path.splitext(filepath)[1]}")
        warn_msg("Supported: .py .js .sh .php .rb .pl .lua .r .c .cpp .java")
        return

    size, lines = get_file_info(filepath)
    lang_name   = lang_info["name"]
    cmd_name    = lang_info["cmd"]

    # Show file info
    print(f"\n  {O}{BLD}File Info:{RST}")
    info_msg(f"File     : {os.path.basename(filepath)}")
    info_msg(f"Language : {lang_name}")
    info_msg(f"Size     : {size} bytes  |  Lines: {lines}")
    info_msg(f"Runner   : {cmd_name}")
    if args:
        info_msg(f"Args     : {args}")
    print()

    # Check interpreter installed
    if not check_interpreter(cmd_name):
        err_msg(f"{cmd_name} is not installed.")
        warn_msg(f"Install with: apt install {lang_info.get('install', cmd_name)}")
        return

    save_last(filepath)

    # Compiled languages
    if lang_info.get("compile"):
        result = run_compiled(filepath, lang_info, args)
        if result is None:
            return
        output, errors, exit_code, duration = result
    else:
        cmd = [cmd_name, filepath] + (args.split() if args else [])
        output, errors, exit_code, duration = _execute(cmd, filepath)

    # Save log
    log_path = save_log(filepath, args, output, errors, duration, exit_code)
    if log_path:
        ok_msg(f"Log saved : {log_path}")
