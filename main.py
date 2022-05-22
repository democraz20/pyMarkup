import colorama
from colorama import Fore, Back, Style
from getmod import *
colorama.init()

# open a file and read it"""
with open('text.txt') as f:
    read = f.readlines()
#print(read)

for text in read:
    # print(getBoolEach('#', text))
    colors = getColor(text)
    # print(colors)
    if colors == None:
        print(pureText(text))
    elif len(colors) == 2:
        print(colorStr(colors[0]) + colorStr(colors[1]) + pureText(text))
    elif len(colors) == 1:
        print(colorStr(colors[0]) + pureText(text))

    print(Style.RESET_ALL, end="")
    # print(pureText(text))
    #print(pureText(text))