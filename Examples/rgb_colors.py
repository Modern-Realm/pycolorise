from pycolorise import Color, RGB
from pycolorise.enums import FontStyles

# RGB colors
a = Color("Hello world", fg=RGB(0, 128, 128), style=FontStyles.bold)
print(a)

# hex colors
b = Color("Hello world", fg=RGB.from_hex("9a6324"))
print(b)
