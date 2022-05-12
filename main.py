import colorama
from colorama import Fore, Back, Style

from colorFromStr import colorFromStr

from getMod import *


colorama.init(autoreset=True)
#text = open("main.txt", "r")
#text = text.read()

#Fore.GREEN,Back.RED=>

text = """this is the header text

Fore.BLACK,Back.WHITE=>this is a line of text with 2 effects [noEnd]
 (both background and foreground)
Fore.GREEN=>and this is some fore greentext

Example of multicolored line text : [noEnd]
Fore.YELLOW=>hello there

Fore.RED=>Back + Fore in same line [noEnd]
is here"""
#print(text.split("\n"))
#print(f"{text}")

for x in text.split("\n"):
    onlyText = plainText(x)
    color = colorT(x)
    end = endT(x)


    #has colors
    if color[0][0] == "Fore" or color[0][0] == "Back":
        #has 2 colors
        if len(color) == 2:
            for i in onlyText:
                print(colorFromStr(color[0])+colorFromStr(color[1])+i+" ", end="")
        elif len(color) == 1:
            for i in onlyText:
                print(colorFromStr(color[0])+i+" ", end="")



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

            
