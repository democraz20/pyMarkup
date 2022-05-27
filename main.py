import renderer
from renderer import renderer, returnLink
import pyfiglet
#open file and read
with open("text.txt", "r") as f:
    text = f.readlines()

# print(pyfiglet.figlet_format("printing from renderer file"))
    
while True:
    links = []
    renderer(text)
    for i in text:
        link = returnLink(i)
        if not link:
            pass
        else: links.append(link)
    pass
    cmd = input("-> ")
    if cmd == "exit":
        break
    else:
        try:
            cmd = int(cmd)
        except:
            print("Invalid command")
            continue
        print(links[cmd])
        linktype = links[cmd].split(":")
        if "http" in linktype[0]:
            import webbrowser
            webbrowser.open(links[cmd])
        elif "pymku" in linktype[0]:
            # open file
            with open(linktype[1], "r") as f:
                text = f.readlines()