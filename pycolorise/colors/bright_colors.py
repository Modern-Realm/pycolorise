from typing import Any

from pycolorise.base import Color
from pycolorise.enums import Colors

__all__ = [
    "DarkGrey",
    "BrightRed",
    "BrightGreen",
    "BrightYellow",
    "BrightBlue",
    "BrightCyan"
]


class DarkGrey(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to DarkGrey color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.dark_grey, **kwargs)


class BrightRed(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Bright Red color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.bright_red, **kwargs)


class BrightGreen(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Bright Green color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.bright_green, **kwargs)


class BrightYellow(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Yellow color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.yellow, **kwargs)


class BrightBlue(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Bright Blue color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.bright_blue, **kwargs)


class BrightCyan(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Bright Cyan color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.bright_cyan, **kwargs)
