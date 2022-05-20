import colorama
import pyfiglet
from colorama import Fore, Back, Style

from colorFromStr import colorStr

from getMod import *
from utils import checkEnd

    
colorama.init(autoreset=True)
#text = open("main.txt", "r")
#text = text.read()

#Fore.GREEN,Back.RED=>

text = """# <Fore.CYAN>this is the header text with colors
<Fore.BLACK,Back.WHITE>this is a line of text with 2 effects <noEnd>
 (both background and foreground)
<Fore.GREEN>and this is some fore greentext

line with no modifiers
Example of multicolored line text : <noEnd>
<Fore.YELLOW>hello there

<Fore.RED>Back + Fore in same line <noEnd>
 is here"""
#print(text.split("\n"))
#print(f"{text}")

for x in text.split("\n"):
    onlyText = plainText(x)
    color = colorT(x)
    end = endT(x)
    header = isHeader(x)


    #has colors
    if color[0][0] == "Fore" or color[0][0] == "Back":
        #has 2 colors
        if len(color) == 2:
            if header:
                sum = " ".join(onlyText)
                sum = colorStr(color[0]) + colorStr(color[1]) + pyfiglet.figlet_format(sum)
                print(sum, end="")
            else:
                sum = colorStr(color[0]) + colorStr(color[1]) + " ".join(onlyText)
                print(sum, end="")
        elif len(color) == 1:
            if header:
                sum = " ".join(onlyText)
                sum = colorStr(color[0]) + pyfiglet.figlet_format(sum)
                print(sum, end="")
            else:
                sum = colorStr(color[0]) + " ".join(onlyText)
                print(sum, end="")
        checkEnd(x)
    elif color[0] == "noColor":
        if header:
            sum = pyfiglet.figlet_format(" ".join(onlyText))
            print(sum, end="")
        else:
            #log(onlyText)
            print(" ".join(onlyText), end="")
        checkEnd(x)

            
