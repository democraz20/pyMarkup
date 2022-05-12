import colorama
from colorama import Fore, Back, Style

from colorFromStr import colorFromStr

from getMod import *


colorama.init(autoreset=True)
#text = open("main.txt", "r")
#text = text.read()

text = """this is the header text

Fore.GREEN=>and this is some fore greentext

Example of multicolored line text : [noEnd]
Fore.YELLOW=>hello there

Fore.RED=>Back + Fore in same line [noEnd]
is coming"""
#print(text.split("\n"))
#print(f"{text}")

for x in text.split("\n"):
    onlyText = plainText(x)
    color = colorT(x)
    end = endT(x)

    if color[0] == "Fore" or color[0] == "Back":
        print(colorFromStr(color[1]), end="")
        for i in onlyText:
            print(colorFromStr(color[0]+"."+color[1])+i+" ", end="")
        if end == True:
            print()
        elif end == False:
            print(end="")
    elif color[0] == "noColor":
        for i in onlyText:
            print(i+" ", end="")
        if end == True:
            print()
        elif end == False:
            print(end="")

            