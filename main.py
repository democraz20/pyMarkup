import renderer
from renderer import renderer
import pyfiglet
#open file and read
with open("text.txt", "r") as f:
    text = f.readlines()


print(pyfiglet.figlet_format("printing from renderer file"))
renderer(text)