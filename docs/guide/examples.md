# Examples

```python
from pycolorise.colors import *
from pycolorise.bgColors import *
from pycolorise.styles import *

print("• Foreground colors")
print(
    Red("red"), BrightRed("bred"),
    Green("green"), BrightGreen("bgreen"),
    Blue("blue"), BrightBlue("bblue"),
    Cyan("cyan"), BrightCyan("bcyan")
)

print(
    Yellow("yellow"), BrightYellow("byellow"),
    DarkGrey("bgrey"), Grey("grey"),
    Black("black"), White("white"),
    Purple("purple"), Pink("pink"),
)

print("\n• Background colors")
print(
    BgRed("red"), BgBrightRed("bred"),
    BgGreen("green"), BgBrightGreen("bgreen"),
    BgBlue("blue"), BgBrightBlue("bblue"),
    BgCyan("cyan"), BgBrightCyan("bcyan")
)

print(
    BgYellow("yellow"), BgBrightYellow("byellow"),
    BgDarkGrey("bgrey"), BgGrey("grey"),
    BgBlack("black"), BgWhite("white"),
    BgPurple("purple"), BgPink("pink"),
)

print("\n• Font styles")
print(
    Default("default"), Bold("bold"),
    Dim("dim"), Italic("italic"),
    Underline("underline"), Blink("blink"),
    RapidBlink("rapid_blink")
)

print(
    StrikeThrough("strike through"),
    Framed("framed"), Inverse("inverse"),
    Encircled("encircled"), Hidden("hidden"),
    OverLined("over lined")
)
```

Output:

<img src="https://github.com/Modern-Realm/pycolorise/blob/main/images/output-1.png" alt="output">
