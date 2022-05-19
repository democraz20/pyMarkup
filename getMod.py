from utils import log

def plainText(text):
    getColor = text.split(">")
    if len(getColor) != 1:
        getEnd = getColor[1].split(" ")
    else:
        getEnd = text.split(" ")
    if getEnd[-1] == "<noEnd>":
        getEnd.pop(len(getEnd)-1)

    return getEnd

def colorT(text):
    getColor = text.split(">")
    if len(getColor) == 3:
        getColor.pop(2)
    #log(getColor)
    #log(len(getColor))
    if isHeader(getColor[0]):
        holder = getColor[0].replace("# ", "")
        getColor[0] = holder
        
    holder = getColor[0].lstrip("<")
    getColor[0] = holder
    #if there's atleast one color specified
    if len(getColor) == 2:
        eachColor = getColor[0].split(",")
        if len(eachColor) == 2:
            res = []
            res.append(eachColor[0].split("."))
            res.append(eachColor[1].split("."))
            return res
        elif len(eachColor) == 1:
            res = []
            res.append(eachColor[0].split("."))
            return res
    elif len(getColor) == 1:
        return ["noColor"]

def endT(text):
    getEnd = text.split(" ")
    if getEnd[-1] == "<noEnd>":
        return False
    elif getEnd[-1] != "<noEnd>":
        return True

def isHeader(text):
    firstSpaces = text.split(" ")
    if firstSpaces[0] == "#":
        return True
    else:
        return False