from enum import Enum
from typing import TypeVar, Tuple

__all__ = [
    "ColorString",
    "Colors",
    "BgColors",
    "FontStyles",
    "MISSING"
]

ColorString = TypeVar("ColorString", str, str)


class BaseEnum(Enum):
    """
    Base enum for Colors, BgColors and FontStyles
    """

    def __str__(self) -> str:
        """

        Returns:
            code: color code
        """

        return str(self.value)

    @property
    def items(self) -> Tuple[str, int]:
        """

        Returns:
            color name and code
        """

        return self.name, self.value


class Colors(BaseEnum):
    """
    Foreground colors or font colors

    Properties:
      - black
      - dark_grey
      - red
      - bright_red
      - green
      - bright_green
      - orange
      - yellow
      - blue
      - bright_blue
      - purple
      - pink
      - cyan
      - bright_cyan
      - grey
      - white
    """

    black = 30
    dark_grey = 90

    red = 31
    bright_red = 91

    green = 32
    bright_green = 92

    orange = 33
    yellow = 93

    blue = 34
    bright_blue = 94

    purple = 35
    pink = 95

    cyan = 36
    bright_cyan = 96

    grey = 37
    white = 97


class BgColors(BaseEnum):
    """
    Background colors

    Properties:
      - black
      - dark_grey
      - red
      - bright_red
      - green
      - bright_green
      - orange
      - yellow
      - blue
      - bright_blue
      - purple
      - pink
      - cyan
      - bright_cyan
      - grey
      - white
    """

    black = 40
    dark_grey = 100

    red = 41
    bright_red = 101

    green = 42
    bright_green = 102

    yellow = 43
    bright_yellow = 103

    blue = 44
    bright_blue = 104

    purple = 45
    pink = 105

    cyan = 46
    bright_cyan = 106

    grey = 47
    white = 107


class FontStyles(BaseEnum):
    """
    Font styles

    Properties:
      - default
      - bold
      - dim
      - italic
      - underline
      - blink
      - rapid_blink
      - inverse
      - hidden
      - strike_through
      - framed
      - encircled
      - overlined
    """

    default = 0
    bold = 1
    dim = 2
    italic = 3
    underline = 4
    blink = 5
    rapid_blink = 6
    inverse = 7
    hidden = 8
    strike_through = 9
    framed = 51
    encircled = 52
    overlined = 53


class _Missing:
    def __repr__(self) -> str:
        return "..."


MISSING = _Missing()
