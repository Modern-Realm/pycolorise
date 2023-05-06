from typing import Any

from pycolorise.base import Color
from pycolorise.enums import FontStyles

__all__ = [
    "Style",
    "Default",
    "Dim",
    "Bold",
    "Italic",
    "Underline",
    "Blink",
    "RapidBlink",
    "StrikeThrough",
    "Framed",
    "Inverse",
    "Encircled",
    "Hidden",
    "OverLined"
]


class Style(Color):
    def __init__(self, content: Any, **kwargs: Any):
        """Base Style decorator

        Args:
            content: string to be colored
            kwargs: arguments same as in `Color`
        """

        super().__init__(content=content, **kwargs)


class Default(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Default font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.default, **kwargs)


class Dim(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Dim font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.dim, **kwargs)


class Bold(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Bold font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.bold, **kwargs)


class Italic(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Italic font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.italic, **kwargs)


class Underline(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Underline font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.underline, **kwargs)


class Blink(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Blink font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`

        """

        super().__init__(content=content, style=FontStyles.blink, **kwargs)


class RapidBlink(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Rapid Blink font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.rapid_blink, **kwargs)


class Framed(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Framed font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.framed, **kwargs)


class StrikeThrough(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Strike Through font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.strike_through, **kwargs)


class Inverse(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Inverse font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.inverse, **kwargs)


class Encircled(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Encircled font

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.encircled, **kwargs)


class Hidden(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Hidden font, may not work in all terminals

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.hidden, **kwargs)


class OverLined(Style):
    def __init__(self, content: Any, **kwargs: Any):
        """Converts string to Over Lined font, may not work in all terminals

        Args:
            content: string to be styled
            kwargs: same as arguments in `Color`
        """

        super().__init__(content=content, style=FontStyles.overlined, **kwargs)
