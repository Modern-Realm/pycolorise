# Examples for Template

```python
from pycolorise import Template, RGB
from pycolorise.enums import FontStyles

f1 = Template(
    fg=RGB.from_hex("#9a6324"),  # brown color
    style=FontStyles.bold
)

f2 = Template(
    fg=RGB(0, 128, 128),  # Teal color
    style=(FontStyles.bold, FontStyles.italic)
)

print(f1("hello") + f1("world"))

print(f1("this"), f2("is"), f1("the"), f1("example"), f2("for"), f1("using"), f2("template"))
```

Output:

![output](/pycolorise/images/templates.png)
