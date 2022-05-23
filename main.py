from itertools import tee
from re import T
import colorama
from colorama import Fore, Back, Style
from getmod import *
colorama.init(autoreset=True)

# open a file and read it"""
with open('text.txt') as f:
    read = f.readlines()
#print(read)

for text in read:
    # print(getBoolEach('#', text))
    colors = getColor(text)
    header = getBoolEach("#", text)
    noEnd = getBoolEach("noEnd", text)
    # print(colors)
    if colors == None:
        sum = " ".join(pureText(text))
        print(sum, end="")
    elif len(colors) == 2:
        sum = colorStr(colors[0]) + colorStr(colors[1]) + " ".join(pureText(text))
        print(sum, end="")
    elif len(colors) == 1:
        sum = colorStr(colors[0]) + " ".join(pureText(text))
        print(sum, end="")
    
    checkEnd(text)
    # print(Style.RESET_ALL, end="")
    # checkEnd(text)
    # print(pureText(text))
    #print(pureText(text))