'''from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()'''

from PIL import Image
from utils.Map import Map
test = Map(503)
img = Image.new('RGB', (test.get_length(), test.get_height()), color='white')
starting_coords = (3, 100)
nding_coords = (267, 490)
a = test.get_route(starting_coords[0], starting_coords[1], nding_coords[0], nding_coords[1])
print(a)
if len(a) == 0:
    exit("Empty pathing")
for a1 in a:
    img.putpixel(a1, (0, 255, 0))
img.putpixel(starting_coords, (255, 0, 0))
img.putpixel(nding_coords, (255, 0, 0))
img.save('map.png')
