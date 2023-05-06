from pycolorise.constants import *

print(purple + "foreground colors:" + end)
print(red + "red", blue + bold + "blue" + end)
print(bright_red + "red" + black + bg_cyan + "cyan" + end)

print(purple + "background colors:" + end)
print(bg_red + "red" + end)
print(bg_bright_cyan + "bcyan" + end)

print(purple + "RGB colors:" + end)
print(rgbColor(1, 255, 1) + "green", end)
print(rgbBgColor(1, 255, 1) + "bg_green" + end)

print(purple + "hex colors:" + end)
print(hexColor("#ffa500") + "orange" + end)
print(hexBgColor(0xff4fff) + "pink" + end)
