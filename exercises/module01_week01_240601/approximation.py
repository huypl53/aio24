from typing import Callable, Any
import sys
import os

current_path = sys.path[0]
aio_path = current_path.rsplit(os.path.sep, 2)[0]
sys.path.append(aio_path)

from aio24.validator import InputTypeValidator, PositiveInputValidator
from aio24 import is_number


@InputTypeValidator(int)
@PositiveInputValidator()
def fractorial(x: int) -> int:
    if x == 2:
        return x
    if x < 2:
        return 1
    return x * fractorial(x - 1)


def sum_loop(func: Callable):
    def wrapper(*args, **kwargs):
        sum = 0
        n = kwargs["n"]
        for i in range(n):
            kwargs.update({"n": i})
            sum += func(*args, **kwargs)
        return sum

    return wrapper


@sum_loop
@InputTypeValidator((float, int), int)
def get_approx_sin(*, x: float, n: int):
    return ((-1) ** n) * ((x ** (2 * n + 1)) / fractorial(2 * n + 1))


@sum_loop
@InputTypeValidator((float, int), int)
def get_approx_cos(*, x: float, n: int):
    return ((-1) ** n) * ((x ** (2 * n)) / fractorial(2 * n))


@sum_loop
@InputTypeValidator((float, int), int)
def get_approx_sinh(*, x: float, n: int):
    return (x ** (2 * n + 1)) / fractorial(2 * n + 1)


@sum_loop
@InputTypeValidator((float, int), int)
def get_approx_cosh(*, x: float, n: int):
    return (x ** (2 * n)) / fractorial(2 * n)


if __name__ == "__main__":
    x = input("Input x = ")
    if not is_number(x):
        raise ValueError(f"{x} has to be number")
    x = float(x)

    n = input("Input n = ")
    if not is_number(n):
        raise ValueError(f"{n} has to be number")
    n = int(n)

    sin_x = get_approx_sin(x=x, n=n)
    cos_x = get_approx_cos(x=x, n=n)
    sinh_x = get_approx_sinh(x=x, n=n)
    cosh_x = get_approx_cosh(x=x, n=n)

    print(f"sin({x}) = {sin_x}")
    print(f"cos({x}) = {cos_x}")
    print(f"sinh({x}) = {sinh_x}")
    print(f"cosh({x}) = {cosh_x}")
