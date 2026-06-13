#!/data/data/com.termux/files/usr/bin/bash
# ─────────────────────────────────────────
#  X-RUNNER — installer.sh
#  Dev: Md. Mainul Islam (CODEX-M41NUL)
# ─────────────────────────────────────────

R="\033[91m"; G="\033[92m"; Y="\033[93m"
O="\033[38;5;208m"; W="\033[97m"; B="\033[1m"; DIM="\033[2m"; RST="\033[0m"

clear

# Colorful pixel banner
echo -e "${R}${B} ██╗${RST}  ${Y}${B}██╗${RST}      ${G}${B}██████╗ ${RST} ${O}${B}██╗   ██╗${RST} ${R}${B}███╗   ██╗${RST} ${Y}${B}███╗   ██╗${RST} ${G}${B}███████╗${RST} ${O}${B}██████╗${RST} "
echo -e "${R}${B} ╚██╗${RST}${Y}${B}██╔╝${RST}      ${G}${B}██╔══██╗${RST} ${O}${B}██║   ██║${RST} ${R}${B}████╗  ██║${RST} ${Y}${B}████╗  ██║${RST} ${G}${B}██╔════╝${RST} ${O}${B}██╔══██╗${RST}"
echo -e "  ${Y}${B}╚███╔╝${RST}  ${G}${B}█████╗${RST} ${G}${B}██████╔╝${RST} ${O}${B}██║   ██║${RST} ${R}${B}██╔██╗ ██║${RST} ${Y}${B}██╔██╗ ██║${RST} ${G}${B}█████╗  ${RST} ${O}${B}██████╔╝${RST}"
echo -e "  ${Y}${B}██╔██╗${RST}  ${G}${B}╚════╝${RST} ${G}${B}██╔══██╗${RST} ${O}${B}██║   ██║${RST} ${R}${B}██║╚██╗██║${RST} ${Y}${B}██║╚██╗██║${RST} ${G}${B}██╔══╝  ${RST} ${O}${B}██╔══██╗${RST}"
echo -e " ${R}${B}██╔╝ ██╗${RST}      ${G}${B}██║  ██║${RST} ${O}${B}╚██████╔╝${RST} ${R}${B}██║ ╚████║${RST} ${Y}${B}██║ ╚████║${RST} ${G}${B}███████╗${RST} ${O}${B}██║  ██║${RST}"
echo -e " ${R}${B}╚═╝  ╚═╝${RST}      ${G}${B}╚═╝  ╚═╝${RST} ${O}${B} ╚═════╝ ${RST} ${R}${B}╚═╝  ╚═══╝${RST} ${Y}${B}╚═╝  ╚═══╝${RST} ${G}${B}╚══════╝${RST} ${O}${B}╚═╝  ╚═╝${RST}"
echo -e "${DIM}${W}  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░${RST}"
echo -e "  ${W}[ v1.0.0 ]  ${Y}Multi-Language Script Runner${RST}  ${O}|  CODEX-M41NUL${RST}"
echo ""
echo -e "  ${O}Installer  v1.0.0  |  github.com/M41NUL${RST}"
echo ""
echo -e "  ${O}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RST}"
echo ""

progress_bar() {
    local label="$1" total=35 bar_width=30
    for i in $(seq 1 $total); do
        local filled=$(( bar_width * i / total ))
        local empty=$(( bar_width - filled ))
        local pct=$(( 100 * i / total ))
        local bar="" heavy=$(( filled * 6 / 10 )) med=$(( filled - filled * 6 / 10 ))
        [ $heavy -gt 0 ] && bar+=$(printf '%0.s▓' $(seq 1 $heavy))
        [ $med   -gt 0 ] && bar+=$(printf '%0.s▒' $(seq 1 $med))
        [ $filled -gt 0 ] && bar+="▶"
        [ $empty -gt 0 ]  && bar+=$(printf '%0.s░' $(seq 1 $empty))
        if   [ $pct -lt 40 ]; then bc="${R}"
        elif [ $pct -lt 80 ]; then bc="${Y}"
        else bc="${G}"; fi
        printf "\r  ${W}%-22s${RST}  ${bc}${B}[%s]${RST}  ${W}%3d%%${RST}" "$label" "$bar" "$pct"
        sleep 0.03
    done
    echo ""
}

ok_msg()   { echo -e "  ${G}${B}+${RST}  ${W}$1${RST}"; }
skip_msg() { echo -e "  ${Y}${B}o${RST}  ${DIM}${W}$1  (already installed)${RST}"; }
step_msg() { echo -e "\n  ${O}${B}>${RST}  ${W}$1${RST}"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FLAG_FILE="$SCRIPT_DIR/.installed"
STORAGE_FLAG="$SCRIPT_DIR/.storage_granted"

if [ -f "$FLAG_FILE" ]; then
    echo -e "  ${G}${B}+  Already installed! Launching X-RUNNER...${RST}\n"
    sleep 1; cd "$SCRIPT_DIR"; python main.py; exit 0
fi

step_msg "Updating package lists..."
progress_bar "apt update"
apt update -y -q 2>/dev/null
ok_msg "Package lists updated"

step_msg "Checking Python..."
if command -v python &>/dev/null || command -v python3 &>/dev/null; then
    skip_msg "Python"
else
    progress_bar "Installing python"
    apt install -y -q python 2>/dev/null || apt install -y -q python3 2>/dev/null
    ok_msg "Python installed"
fi

step_msg "Checking pip..."
command -v pip &>/dev/null && skip_msg "pip" || { progress_bar "Installing pip"; apt install -y -q python-pip 2>/dev/null; ok_msg "pip installed"; }

step_msg "Checking git..."
command -v git &>/dev/null && skip_msg "git" || { progress_bar "Installing git"; apt install -y -q git 2>/dev/null; ok_msg "git installed"; }

step_msg "Checking node..."
command -v node &>/dev/null && skip_msg "node" || { progress_bar "Installing nodejs"; apt install -y -q nodejs 2>/dev/null; ok_msg "nodejs installed"; }

echo ""
echo -e "  ${O}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RST}"

if [ -f "$STORAGE_FLAG" ] || [ -d "/sdcard/Android" ]; then
    echo -e "\n  ${G}${B}+  Storage permission already granted. Skipping.${RST}"
else
    echo -e "\n  ${G}${B}  Requesting Android storage permission...${RST}"
    echo -e "  ${W}A dialog will appear -- tap ALLOW to enable /sdcard access.${RST}\n"
    termux-setup-storage; sleep 2
    touch "$STORAGE_FLAG"
    ok_msg "Storage permission granted"
fi

touch "$FLAG_FILE"

echo ""
echo -e "  ${O}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RST}"
echo -e "\n  ${G}${B}+  Installation complete!${RST}\n"

for i in 3 2 1; do
    printf "\r  ${O}${B}Starting X-RUNNER in ${G}$i${O}...${RST}   "
    sleep 1
done
echo -e "\r  ${G}${B}Launching X-RUNNER...${RST}              \n"

cd "$SCRIPT_DIR"
python main.py
