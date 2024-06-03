from typing import Any, Type


def is_number(x: Any) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


def get_std_input(msg: str, input_type: Type) -> Any:
    x = input(msg)
    try:
        return input_type(x)
    except Exception:
        raise ValueError(f"{x} must be {input_type}")
