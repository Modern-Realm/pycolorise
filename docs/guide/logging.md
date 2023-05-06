# Customise logger with colors

```python
import logging

from pycolorise.colors import *
from pycolorise import Color, RGB
from pycolorise.enums import FontStyles

asctime = Color("%(asctime)s", fg=RGB(0, 128, 128))  # Teal color
name = Blue("%(name)s")
level = Red("%(levelname)s", style=FontStyles.bold)
msg = Purple("%(message)s", style=FontStyles.italic)

logging.basicConfig(
    format=f"{asctime} - {name} - {level} - {msg}",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

Output:

<img src="https://github.com/Modern-Realm/pycolorise/blob/main/images/output-3.png" alt="output">
