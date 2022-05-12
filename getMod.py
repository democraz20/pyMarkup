def plainText(text):
    getColor = text.split("=>")
    if len(getColor) != 1:
        getEnd = getColor[1].split(" ")
    else:
        getEnd = text.split(" ")
    if getEnd[-1] == "[noEnd]":
        getEnd.pop(len(getEnd)-1)

    return getEnd

def colorT(text):
    getColor = text.split("=>")
    if len(getColor) != 1:
        color = getColor[0].split(".")
        res = [color[0], color[1]]
        return res
    elif len(getColor) == 1:
        return ["noColor"]

def endT(text):
    getEnd = text.split(" ")
    if getEnd[-1] == "[noEnd]":
        return False
    elif getEnd[-1] != "[noEnd]":
        return True
