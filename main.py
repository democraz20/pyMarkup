import colorama
from getmod import *
colorama.init()

# open a file and read it"""
with open('text.txt') as f:
    read = f.readlines()
#print(read)

for text in read:
    #print(pureText(text))
    print(pureText(text))