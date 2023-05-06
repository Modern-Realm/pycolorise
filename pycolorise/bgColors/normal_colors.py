from typing import Any

from pycolorise.base import Color
from pycolorise.enums import BgColors

__all__ = [
    "BgBlack",
    "BgRed",
    "BgGreen",
    "BgYellow",
    "BgBlue",
    "BgPurple",
    "BgCyan",
    "BgWhite",
    "BgGrey",
    "BgPink"
]


class BgBlack(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Black color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.black, **kwargs)


class BgRed(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Red color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.red, **kwargs)


class BgGreen(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Green color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.green, **kwargs)


class BgYellow(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Yellow color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.yellow, **kwargs)


class BgBlue(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Blue color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.blue, **kwargs)


class BgPurple(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Purple color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.purple, **kwargs)


class BgCyan(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Cyan color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.cyan, **kwargs)


class BgWhite(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to White color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.white, **kwargs)


class BgGrey(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Grey color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.grey, **kwargs)


class BgPink(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string's background to Pink color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, bg=BgColors.pink, **kwargs)
