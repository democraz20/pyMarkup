from itertools import tee
from re import T
import colorama
from colorama import Fore, Back, Style
from getmod import *
import pyfiglet
colorama.init(autoreset=True)

# open a file and read it"""
with open('text.txt', 'r') as f:
    read = f.readlines()
#print(read)

for text in read:
    # print(getBoolEach('#', text))
    colors = getColor(text)
    header = getBoolEach("#", text)
    noEnd = getBoolEach("noEnd", text)
    figfont = getHeaderFont(text)
    if not figfont:
        figfont = "standard"
    # print(colors)
    sum = " ".join(pureText(text))
    if header:
        try:
            sum = pyfiglet.figlet_format(sum, font=figfont)
        except:
            print(f"{Fore.RED} Error : header font not found")
    if colors == None:
        sum = sum
        print(sum, end="")
    elif len(colors) == 2:
        sum = colorStr(colors[0]) + colorStr(colors[1]) + sum
        print(sum, end="")
    elif len(colors) == 1:
        sum = colorStr(colors[0]) + sum
        print(sum, end="")
    
    checkEnd(text)
    # print(Style.RESET_ALL, end="")
    # checkEnd(text)
    # print(pureText(text))
    #print(pureText(text))