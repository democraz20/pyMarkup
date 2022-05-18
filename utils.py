from colorama import Fore, Back, Style

def checkEnd(text):
    from getMod import endT
    end = endT(text)
    if end == True:
        print()
    elif end == False:
        print(end="")

def log(text):
    print(Fore.YELLOW+"[LOG] : ", end="")
    print(text)