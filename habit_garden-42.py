# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: HabitGarden
import os

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    DEFAULT = "\033[39m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

# Check if terminal supports colors
_supports_colors = hasattr(os, 'termios') and os.isatty(0)

def color(text, color_code):
    """Apply color to text if terminal supports it."""
    if _supports_colors:
        return f"{color_code}{text}{Colors.RESET}"
    return text

def bold(text):
    """Make text bold if terminal supports it."""
    if _supports_colors:
        return f"{Colors.BOLD}{text}{Colors.RESET}"
    return text

def dim(text):
    """Make text dim if terminal supports it."""
    if _supports_colors:
        return f"{Colors.DIM}{text}{Colors.RESET}"
    return text

def underlined(text):
    """Underline text if terminal supports it."""
    if _supports_colors:
        return f"{Colors.UNDERLINE}{text}{Colors.RESET}"
    return text

# Usage examples:
# print(color("Hello World", Colors.GREEN))
# print(bold("Important message"))
# print(dim("Subtle information"))
# print(underlined("Section title"))
