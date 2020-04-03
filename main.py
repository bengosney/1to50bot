from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber
import pyautogui
import time

x1 = 999999
x2 = 0

y1 = 999999
y2 = 0

print("finding puzzle bounds")
for i in range(1, 26):
    pos = imagesearch(f"./imgs/{i}.png")
    if pos[0] != -1:
        x1 = min(x1, pos[0])
        x2 = max(x2, pos[0])

        y1 = min(y1, pos[1])
        y2 = max(y2, pos[1])
    else:
        print(f"Failed to find {i}")
        exit(0)


print("playing")
grabs = [25, 29, 50]

clicks = []
im = region_grabber((x1, y1, x2 + 100, y2 + 100))
for i in range(1, 51):
    pos = imagesearcharea(f"./imgs/{i}.png", x1, y1, x2 + 200, y2 + 200, im=im)
    if pos[0] != -1:
        #pyautogui.click(pos[0] + 10 + x1, pos[1] + 10 + y1)
        clicks.append([pos[0] + 10 + x1, pos[1] + 10 + y1])
    else:
        print(f"Failed to find {i}")
        exit

    if i in grabs:
        for c in clicks:
            pyautogui.click(c[0], c[1])
        clicks = []
        im = region_grabber((x1, y1, x2 + 100, y2 + 100))

