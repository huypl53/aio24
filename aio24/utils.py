from typing import Any


def is_number(x: Any) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False
