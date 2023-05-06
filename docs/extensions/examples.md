# Examples usage of constants

```python
from pycolorise.constants import *

print(red + "red", blue + bold + "blue" + end)
print(bright_red + "red" + black + bg_cyan + "cyan" + end)

# rgb colors
print(rgbColor(1, 255, 1) + "green", end)
print(rgbBgColor(1, 255, 1) + "bg_green" + end)

# hex colors
print(hexColor("#ffa500") + "orange" + end)
print(hexBgColor(0xff4fff) + "pink" + end)
```

Output:

<img src="https://github.com/Modern-Realm/pycolorise/blob/main/images/constants.png" alt="output">
