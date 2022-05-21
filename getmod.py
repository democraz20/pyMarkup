from logging.config import IDENTIFIER
import re

def getTags(text):
    return re.findall('<(.*?)>', text)

#def getEverything(text):
    #return re.findall('<(.*?)>(.*?)<(.*?)>', text)
def pureText(text):
    #string.filter(char => char !== '<' && char !== '>')
    marker = "*"
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
    res = " ".join(text)
    return res
    #return re.findall('>(.*?)<', text)