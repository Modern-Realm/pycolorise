from typing import Any

from pycolorise.base import Color
from pycolorise.enums import Colors

__all__ = [
    "Black",
    "Red",
    "Green",
    "Yellow",
    "Blue",
    "Purple",
    "Cyan",
    "White",
    "Grey",
    "Pink"
]


class Black(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Black color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.black, **kwargs)


class Red(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Red color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.red, **kwargs)


class Green(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Green color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.green, **kwargs)


class Yellow(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Yellow color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.orange, **kwargs)


class Blue(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Blue color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.blue, **kwargs)


class Purple(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Purple color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.purple, **kwargs)


class Cyan(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Cyan color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.cyan, **kwargs)


class White(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to White color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.white, **kwargs)


class Grey(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Grey color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.grey, **kwargs)


class Pink(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Pink color

        Args:
            content: string to be colored
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, fg=Colors.pink, **kwargs)
