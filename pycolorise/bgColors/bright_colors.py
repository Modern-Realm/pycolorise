from typing import Any

from pycolorise.base import Color
from pycolorise.enums import BgColors

__all__ = [
    "BgDarkGrey",
    "BgBrightRed",
    "BgBrightGreen",
    "BgBrightYellow",
    "BgBrightBlue",
    "BgBrightCyan"
]


class BgDarkGrey(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to DarkGrey color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.dark_grey, **kwargs)


class BgBrightRed(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Bright Red color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.bright_red, **kwargs)


class BgBrightGreen(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Bright Green color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.bright_green, **kwargs)


class BgBrightYellow(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Yellow color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.bright_yellow, **kwargs)


class BgBrightBlue(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Bright Blue color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.bright_blue, **kwargs)


class BgBrightCyan(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Bright Cyan color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.bright_cyan, **kwargs)
