# from logging.config import IDENTIFIER
import re
from colorFromStr import colorStr
from colorama import Style

def getTags(text):
    return re.findall('<(.*?)>', text)
    #regex

#def getEverything(text):
    #return re.findall('<(.*?)>(.*?)<(.*?)>', text)
def pureText(text):
    #string.filter(char => char !== '<' && char !== '>')
    marker = "§"
    text = text.replace('<', marker)
    text = text.replace('>', ' ')
    text = text.split(" ")
    for i in range(2):
        if text[0].find(marker) != -1:
            text.pop(0)
    #elif len(text) == 1: pass;
    if len(text) > 1:
        if text[-2].find(marker) != -1:
            text.pop(-2)
    text[-1] = text[-1].replace("\n", "")
    #print(text)
    return text
    #return re.findall('>(.*?)<', text)

def getBoolEach(item, text):
    allTags = getTags(text)
    for i in allTags:
        if item in i:
            return True
    return False

def checkEnd(text):
    allTags = getTags(text)
    # print(allTags)
    if len(allTags) >= 1:
        if allTags[-1] == "noEnd":
            print(end="")
        else: 
            print()
    else:
        print()

def getColor(text):
    allTags = getTags(text)
    for i in allTags:
        if i != None:
            if "Fore" in i or "Back" in i:
                i = i.split(",")
                return i

def getHeaderFont(text):
    allTags = getTags(text)
    if len(allTags) >= 1:
        if "#" in allTags[0][0]:
            # print(re.findall('"(.*?)"', allTags[0]))
            return re.findall('"(.*?)"', allTags[0])[0]

def getLink(text):
    allTags = getTags(text)
    if len(allTags) >= 1:
        if "link" in allTags[0]:
            # print(re.findall('"(.*?)"', allTags[0]))
            return re.findall('"(.*?)"', allTags[0])[0]