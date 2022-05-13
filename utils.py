def checkEnd(text):
    from getMod import endT
    end = endT(text)
    if end == True:
        print()
    elif end == False:
        print(end="")
