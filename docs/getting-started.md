# Getting Started

Create a file with '.py ' extension, Like: **main.py**

```python
# For foreground colors
from pycolorise.colors import *
# For background colors
from pycolorise.bgColors import *
# For font styles like: bold, italic, etc
from pycolorise.styles import *

print(Purple("• Foreground colors:"))
print(
    Red("red"), BrightRed("bred"),
    Green("green"), BrightGreen("bgreen")
)

print(Purple("\n• Background colors:"))
print(
    BgRed("red"), BgBrightRed("bred"),
    BgGreen("green"), BgBrightGreen("bgreen")
)

print(Purple("\n• Fonts:"))
print(
    Bold("bold"), Underline("underline"),
    StrikeThrough("strike through"),
    Italic("italic"), Framed("framed")
)
```

Output:

<img src="https://github.com/Modern-Realm/pycolorise/blob/main/images/output-1.png" alt="output">

<hr/>

For more info check [Examples](../guide/examples)
