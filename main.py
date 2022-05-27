import renderer
from renderer import renderer, returnLink
import nav
from nav import navigation
import pyfiglet
#open file and read
with open("text.txt", "r") as f:
    text = f.readlines()

# print(pyfiglet.figlet_format("printing from renderer file"))
navigation(text)