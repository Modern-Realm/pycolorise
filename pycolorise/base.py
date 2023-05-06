from typing import Optional, Any, Union, Tuple, List, TypeVar

from pycolorise.enums import (
    ColorString, Colors,
    BgColors, FontStyles,
    MISSING
)

__all__ = [
    "RGB",
    "ColorTypes",
    "BgColorTypes",
    "FontTypes",
    "Color",
    "Template"
]


class RGB:
    def __init__(self, red: int, green: int, blue: int):
        """RGB color decorator

        Args:
            red: ranges from 0 to 255
            green: ranges from 0 to 255
            blue: ranges from 0 to 255

        Raises:
            ValueError: if the rgb color code is invalid
        """

        if not all([
            0 <= red <= 255, 0 <= green <= 255,
            0 <= blue <= 255
        ]):
            raise ValueError("the rgb color is invalid")

        self.red = red
        self.green = green
        self.blue = blue

    @property
    def value(self) -> Tuple[int, int, int]:
        """

        Returns:
             code: rgb color code
        """

        return self.red, self.green, self.blue

    @classmethod
    def from_hex(cls, color: Union[str, int]):
        """Converts hex color code to rgb color code

        Args:
            color: hex color code

        Returns:
            (RGB): RGB color decorator

        Raises:
            ValueError: if the hex color code is invalid

        Examples:
            ```python
            # orange color
            RGB.from_hex("#ffa500")
            RGB.from_hex("ffa500")
            RGB.from_hex(0xffa500)
            ```
        """

        if isinstance(color, str):
            color = color.lstrip("#") if "#" in color else color
            if len(color) != 6:
                raise ValueError(f"Expected hex color code(ex: #ffa500), got {color} instead")

            values = (int(color[i:i + 2], 16) for i in (0, 2, 4))
        else:
            try:
                values = (
                    (color >> 16) & 0xff, (color >> 8) & 0xff,
                    color & 0xff
                )
            except:
                raise ValueError(f"Expected hex color code(ex: 0xffa500), got {color} instead")

        return cls(*values)

    @property
    def hex_code(self) -> str:
        """
        Returns:
             code: hex color code
        """

        return '#' + ("%02x%02x%02x" % self.value)

    def __repr__(self) -> str:
        r, g, b = self.value
        return f"<{__class__.__module__}.{__class__.__name__}({r}, {g}, {b})>"


ColorTypes = TypeVar("ColorTypes", Colors, RGB, None)
BgColorTypes = TypeVar("BgColorTypes", BgColors, RGB, None)
FontTypes = TypeVar("FontTypes", FontStyles, Tuple[FontStyles, ...], List[FontStyles], None)


class Color:
    def __init__(
            self, content: Any,
            fg: ColorTypes = None,
            bg: BgColorTypes = None,
            style: FontTypes = None
    ):
        """Color decorator

        Args:
            content: string to be colored
            fg: font color (or) foreground color
            bg: background color
            style: font style
        """

        self.end: ColorString = "\x1b[0m"
        self.reset = self.end
        self._cstring: ColorString = "\x1b[%sm"

        self.content = str(content)
        self.fg: Optional[ColorTypes] = fg
        self.bg: Optional[BgColorTypes] = bg
        self.style: Optional[FontTypes] = style

    def _format(self) -> ColorString:
        fg = self.fg
        bg = self.bg
        style = self.style
        if isinstance(self.fg, RGB):
            r, g, b = self.fg.value
            fg = f"38;2;{r};{g};{b}"
        if isinstance(self.bg, RGB):
            r, g, b = self.bg.value
            bg = f"48;2;{r};{g};{b}"
        if isinstance(self.style, tuple) or isinstance(self.style, list):
            if len(self.style) == 0:
                style = FontStyles.default
            else:
                style = ';'.join([str(val) for val in self.style])

        args = [style] if style is not None else []
        if fg is None and bg is not None:
            args.append(bg)
        elif bg is None and fg is not None:
            args.append(fg)
        else:
            args += [fg, bg]

        values = ';'.join([str(arg) for arg in args if arg is not None])
        return (self._cstring % values) + self.content + self.end

    def replace(
            self, value: Any = MISSING,
            fg: ColorTypes = MISSING,
            bg: BgColorTypes = MISSING,
            style: FontTypes = MISSING
    ):
        """Replaces the properties

        Args:
            value: string to be colored
            fg: font color (or) foreground color
            bg: background color
            style: font style
        """

        if value != MISSING:
            self.content = value
        if fg != MISSING:
            self.fg = fg
        if bg != MISSING:
            self.bg = bg
        if style != MISSING:
            self.style = style

    @property
    def value(self) -> ColorString:
        """
        Returns:
            colored string
        """

        return self._format()

    @property
    def properties(self) -> Tuple[ColorTypes, BgColorTypes, FontTypes]:
        """Properties of the string/font

        Returns:
             foreground, background color and font style
        """

        return self.fg, self.bg, self.style

    @staticmethod
    def _check(color):
        if not isinstance(color, Color):
            raise ValueError(f"expected <class 'Color'>, got {type(color)} instead")

    def __str__(self) -> ColorString:
        """
        Returns:
             colored string
        """

        return self._format()

    def __repr__(self) -> str:
        return repr(self.value)

    def __len__(self) -> int:
        """
        Returns:
             length: length of the string
        """

        return len(self.content)

    def __add__(self, color: Any) -> ColorString:
        """ Concatenates two colors

        Args:
            color: color decorator or string

        Returns:
            colored string

        Raises:
            ValueError: if the color is not `Color` type and not string
        """

        if isinstance(color, str):
            return self.value + color

        self._check(color)
        if self.properties == color.properties:
            return self.value.removesuffix(self.end) + color.content + self.end
        else:
            return self.value + color.value

    def __eq__(self, color: Any) -> bool:
        """Compares the two Colors properties and values

        Args:
            color: color decorator or normal string

        Returns:
             `True` if the properties & values are same else `False`

        Raises:
            ValueError: if the color is not `Color` type
        """

        self._check(color)

        return self.value == color.value


class Template:
    def __init__(
            self,
            fg: ColorTypes = None,
            bg: BgColorTypes = None,
            style: FontTypes = None
    ):
        """Color/Font template

        Args:
            fg: font color (or) foreground color
            bg: background color
            style: font style

        Raises:
           ValueError: if no argument is passed

        Examples:
            ```python
            T1 = Template(fg=Colors.red, style=FontStyles.bold)
            print(T1("hello"), T1("world"))
            ```
        """

        if not any([fg, bg, style]):
            raise ValueError("Excepted atleast one argument, got no arguments")

        self.fg = fg
        self.bg = bg
        self.style = style

    def __call__(self, content: Any) -> Color:
        """ color decorator

        Args:
            content: string to be colored

        Returns:
            color decorator
        """

        return Color(content, self.fg, self.bg, self.style)

    @property
    def properties(self):
        return self.fg, self.bg, self.style

    def edit(
            self,
            fg: ColorTypes = MISSING,
            bg: BgColorTypes = MISSING,
            style: FontTypes = MISSING
    ):
        """Edits the template properties

        Args:
            fg: font color (or) foreground color
            bg: background color
            style: font style
        """

        if fg != MISSING:
            self.fg = fg
        if bg != MISSING:
            self.bg = bg
        if style != MISSING:
            self.style = style

    def __eq__(self, template) -> bool:
        """ compares the two templates

        :param template:
        Returns:
            `True` if the properties are same else `False`

        Raises:
            ValueError: if the color is not `Template` type
        """

        if not isinstance(template, Template):
            raise ValueError(f"expected <class 'Template'>, got {type(template)} instead")

        return self.properties == template.properties
