import math
import os
import sys
from typing import Callable, Dict

current_path = sys.path[0]
aio_path = current_path.rsplit(os.path.sep, 2)[0]
sys.path.append(aio_path)

from aio24.validator.base import InputTypeValidator
from aio24 import is_number


@InputTypeValidator(float)
def get_sigmoid(x: float) -> float:
    return 1 / (1 + math.e ** (-x))


@InputTypeValidator(float)
def get_relu(x: float) -> float:
    if x <= 0:
        return 0
    return x


@InputTypeValidator(float)
def get_elu(x: float, alpha=0.01) -> float:
    if x <= 0:
        return alpha * (math.e**x - 1)
    return x


VALID_ACTIVATIONS: Dict[str, Callable] = {
    "sigmoid": get_sigmoid,
    "relu": get_relu,
    "elu": get_elu,
}


def is_valid_activation(func_name: str) -> bool:
    if func_name in VALID_ACTIVATIONS:
        return True
    return False


def print_activated_feature():
    x = input("Input x = ")
    if not is_number(x):
        raise ValueError(f"{x} has to be number")
    x = float(x)
    activation_func = input(
        f"Input activation Function ({'|'.join(VALID_ACTIVATIONS)}): "
    )
    if not is_valid_activation(activation_func):
        raise ValueError(f"{activation_func} function is not supported")

    y = VALID_ACTIVATIONS[activation_func](x)
    print(f"{activation_func}: f({x}) = {y}")


if __name__ == "__main__":
    print_activated_feature()
