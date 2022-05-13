import colorama
from colorama import Fore, Back, Style
colorama.init()

foredict = {
    "BLACK": Fore.BLACK,
    "RED": Fore.RED,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "BLUE": Fore.BLUE,
    "MAGENTA": Fore.MAGENTA,
    "CYAN": Fore.CYAN,
    "WHITE": Fore.WHITE,
    "RESET": Fore.RESET
}
backdict = {
    "BLACK": Back.BLACK,
    "RED": Back.RED,
    "GREEN": Back.GREEN,
    "YELLOW": Back.YELLOW,
    "BLUE": Back.BLUE,
    "MAGENTA": Back.MAGENTA,
    "CYAN": Back.CYAN,
    "WHITE": Back.WHITE,
    "RESET": Back.RESET
}

def colorStr(text):
    if text[0] == "Fore":
        return foredict[text[1]]
    elif text[0] == "Back":
        return backdict[text[1]]
    else:
        return Style.RESET_ALL