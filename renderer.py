import colorama
from colorama import Fore, Back, Style
import re
import pyfiglet
colorama.init(autoreset=True)

def renderer(textin):
    links = []
    for text in textin:
        # print(getBoolEach('#', text))
        colors = getColor(text)
        header = getBoolEach("#", text)
        noEnd = getBoolEach("noEnd", text)
        figfont = getHeaderFont(text)
        link = getLink(text)

        if not link:
            pass
        else:
            links.append(link)
            print(f"{Fore.CYAN}link : {Fore.GREEN}[{Fore.WHITE}{len(links)-1}{Fore.GREEN}] {Fore.WHITE}", end="")
        if not figfont:
            figfont = "standard"
        # print(colors)
        # print(text)
        sum = " ".join(pureText(text))
        if header:
            try:
                sum = pyfiglet.figlet_format(sum, font=figfont)
            except:
                print(f"{Fore.RED} Error : header font not found")
                print("original text : " + sum)

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

def returnLink(text):
    return getLink(text)

def getTags(text):
    return re.findall('<(.*?)>', text)
    #regex

#def getEverything(text):
    #return re.findall('<(.*?)>(.*?)<(.*?)>', text)
def pureText(text):
    #string.filter(char => char !== '<' && char !== '>')
    # print(text)
    marker = "§"
    text = text.replace('<', marker)
    text = text.replace('>', ' ')
    text = text.split(" ")
    for i in range(2):
        # print(f"{Fore.YELLOW} {len(text)}")
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
    text = text.split(".")
    if text[0] == "Fore":
        return foredict[text[1]]
    elif text[0] == "Back":
        return backdict[text[1]]
    else:
        return Style.RESET_ALL