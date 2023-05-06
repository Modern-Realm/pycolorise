# pycolorise

- Add **colors/fonts** to the terminal
- The terminal colorizer is a tool that improves the visual experience of terminal applications

[![python badge](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/ "Python")

[![CodeQL](https://github.com/Modern-Realm/pycolorise/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Modern-Realm/pycolorise/actions/workflows/codeql-analysis.yml)
[![Generic badge](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/)
![Github License](https://img.shields.io/badge/license-MIT-blue)
![Windows](https://img.shields.io/badge/os-windows-yellow)
![Linux](https://img.shields.io/badge/os-linux-yellow)

Join [Official Discord Server](https://discord.gg/GVMWx5EaAN  "click to Join") for more guidance !

# Features

- It provides **templates** for foreground, background colors and font styles for re-usability.

- It supports **24-bit true colors, RGB, and hex colors**, providing a wide range of color options.

- The colorizer is built using **object-oriented programming** principles, making it highly customizable.

- Developers can easily create their own color schemes to suit their needs.

- The colorizer has **no dependencies**, making it easy to integrate into any project without adding unnecessary
  overhead.

# Installation

For stable version, use below command

```shell
pip install -U pycolorise
```

For latest/beta version, install it using `git`

```shell
pip install -U git+https://github.com/Modern-Realm/pycolorise
```

# Quickstart

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

# Useful Links:

- For more guidance check [Examples](https://github.com/Modern-Realm/pycolorise/tree/main/Examples)
- [Documentation](https://modern-realm.github.io/pycolorise/)
- [Contributing](https://github.com/Modern-Realm/pycolorise/blob/main/.github/CONTRIBUTING.md)
- [Code of Conduct](https://github.com/Modern-Realm/pycolorise/blob/main/.github/CODE_OF_CONDUCT.md)

-----

# Contact Us

- [Discord](https://discord.gg/GVMWx5EaAN) • [Github](https://github.com/skrphenix) • [Gmail](mailto:saikeerthan.keerthan.9@gmail.com)
