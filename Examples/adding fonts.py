from pycolorise.colors import *
from pycolorise.styles import *

# Adding two colors
print(Red("hello") + Purple("world"))

# Adding more than two colors
print(Red("good").value + Purple("morning").value + Green("coders").value)
print(Red("good"), Purple("morning"), Green("coders"))
print(f"{Red('good')} {Purple('morning')} {Green('coders')}")

# Adding two fonts
print(Bold("Hello") + Italic("world"))

# Adding more than two fonts
print(Dim("good").value + Bold("morning").value + Underline("coders").value)
print(Dim("good"), Bold("morning"), Underline("coders"))
print(f"{Dim('good')} {Bold('morning')} {Underline('coders')}")
