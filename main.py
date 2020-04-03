from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber
import pyautogui
import time

minx = 999999
maxx = 0

miny = 999999
maxy = 0

print("finding puzzle bounds")
for i in range(1, 26):
    print(f"Looking for {i}")
    pos = imagesearch(f"./imgs/{i}.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        minx = min(minx, pos[0])
        maxx = max(maxx, pos[0])

        miny = min(miny, pos[1])
        maxy = max(maxy, pos[1])


print("playing")
grabs = [1, 26, 30]

for i in range(1, 51):
    if i in grabs:
        im = region_grabber((minx, miny, maxx + 100, maxy + 100))
        
    print(f"Looking for {i}")
    pos = imagesearcharea(f"./imgs/{i}.png", minx, miny, maxx + 200, maxy + 200, im=im)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.click(pos[0] + 10 + minx, pos[1] + 10 + miny)
    else:
        print("image not found")
