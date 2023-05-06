from pycolorise import RGB
from pycolorise.enums import *

start = "\x1b["

# Foreground colors
black = f"{start}{Colors.black}m"
dark_grey = f"{start}{Colors.dark_grey}m"

red = f"{start}{Colors.red}m"
bright_red = f"{start}{Colors.bright_red}m"

green = f"{start}{Colors.green}m"
bright_green = f"{start}{Colors.bright_green}m"

orange = f"{start}{Colors.orange}m"
yellow = f"{start}{Colors.yellow}m"

blue = f"{start}{Colors.blue}m"
bright_blue = f"{start}{Colors.bright_blue}m"

purple = f"{start}{Colors.purple}m"
pink = f"{start}{Colors.pink}m"

cyan = f"{start}{Colors.cyan}m"
bright_cyan = f"{start}{Colors.bright_cyan}m"

grey = f"{start}{Colors.grey}m"
white = f"{start}{Colors.white}m"

# Background colors
bg_black = f"{start}{BgColors.black}m"
bg_dark_grey = f"{start}{BgColors.dark_grey}m"

bg_red = f"{start}{BgColors.red}m"
bg_bright_red = f"{start}{BgColors.bright_red}m"

bg_green = f"{start}{BgColors.green}m"
bg_bright_green = f"{start}{BgColors.bright_green}m"

bg_orange = f"{start}{BgColors.yellow}m"
bg_yellow = f"{start}{BgColors.bright_yellow}m"

bg_blue = f"{start}{BgColors.blue}m"
bg_bright_blue = f"{start}{BgColors.bright_blue}m"

bg_purple = f"{start}{BgColors.purple}m"
bg_pink = f"{start}{BgColors.pink}m"

bg_cyan = f"{start}{BgColors.cyan}m"
bg_bright_cyan = f"{start}{BgColors.bright_cyan}m"

bg_grey = f"{start}{BgColors.grey}m"
bg_white = f"{start}{BgColors.white}m"

# Font Styles
default = f"{start}{FontStyles.default}m"
bold = f"{start}{FontStyles.bold}m"
dim = f"{start}{FontStyles.dim}m"
italic = f"{start}{FontStyles.italic}m"
underline = f"{start}{FontStyles.underline}m"
blink = f"{start}{FontStyles.blink}m"
rapid_blink = f"{start}{FontStyles.rapid_blink}m"
inverse = f"{start}{FontStyles.inverse}m"
hidden = f"{start}{FontStyles.hidden}m"
strike_through = f"{start}{FontStyles.strike_through}m"
framed = f"{start}{FontStyles.framed}m"
encircled = f"{start}{FontStyles.encircled}m"
overlined = f"{start}{FontStyles.overlined}m"

end = reset = "\x1b[0m"


def rgbColor(_red: int, _green: int, _blue: int) -> str:
    """RGB color decorator

    Args:
        _red: ranges from 0 to 255
        _green: ranges from 0 to 255
        _blue: ranges from 0 to 255

    Returns:
        color: colored string

    Raises:
        ValueError: if the rgb color code is invalid
    """

    _red, _green, _blue = RGB(_red, _green, _blue).value
    return f"{start}38;2;{_red};{_green};{_blue}m"


def rgbBgColor(_red: int, _green: int, _blue: int) -> str:
    """RGB background color decorator

    Args:
        _red: ranges from 0 to 255
        _green: ranges from 0 to 255
        _blue: ranges from 0 to 255

    Returns:
        color: colored string

    Raises:
        ValueError: if the rgb color code is invalid
    """

    _red, _green, _blue = RGB(_red, _green, _blue).value
    return f"{start}48;2;{_red};{_green};{_blue}m"


def hexColor(color: str | int, /) -> str:
    """hex color code decorator

    Args:
        color: hex color code

    Returns:
        color: colored string

    Raises:
        ValueError: if the hex color code is invalid
    """

    _rgb = [str(val) for val in RGB.from_hex(color).value]
    return f"{start}38;2;" + ';'.join(_rgb) + 'm'


def hexBgColor(color: str | int, /) -> str:
    """hex color code decorator

    Args:
        color: hex color code

    Returns:
        color: colored string

    Raises:
        ValueError: if the hex color code is invalid
    """

    _rgb = [str(val) for val in RGB.from_hex(color).value]
    return f"{start}48;2;" + ';'.join(_rgb) + 'm'
