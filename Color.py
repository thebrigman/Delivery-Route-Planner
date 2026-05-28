from enum import Enum


class Color(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ORANGE = "\033[38;2;255;165;0m"
    PINK = "\033[38;2;255;105;180m"
    PURPLE = "\033[38;2;148;0;211m"
    TEAL = "\033[38;2;0;128;128m"
    LIME = "\033[38;2;0;255;0m"
    GOLD = "\033[38;2;255;215;0m"
    SKY_BLUE = "\033[38;2;135;206;235m"
    CORAL = "\033[38;2;255;127;80m"
    LAVENDER = "\033[38;2;230;130;255m"

    def __str__(self):
        return self.value