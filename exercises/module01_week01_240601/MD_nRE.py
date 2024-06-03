import os
import sys

current_path = sys.path[0]
aio_path = current_path.rsplit(os.path.sep, 2)[0]
sys.path.append(aio_path)

from aio24.validator import InputTypeValidator
from aio24 import get_std_input


@InputTypeValidator(float, float, int, int)
def md_nre_single_sample(*, y: float, y_hat: float, n: int, p: int):
    return (y ** (1 / n) - y_hat ** (1 / n)) ** p


if __name__ == "__main__":
    y: float = get_std_input("y = ", float)
    y_hat: float = get_std_input("y_hat = ", float)
    n: int = get_std_input("n = ", int)
    p: int = get_std_input("p = ", int)

    print(md_nre_single_sample(y=y, y_hat=y_hat, n=n, p=p))
