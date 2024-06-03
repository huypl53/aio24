import math
import random
from typing import Callable, Dict, List


def get_mae(Y: List[float], Y_hat: List[float]) -> float:
    assert len(Y) == len(Y_hat)
    n = len(Y)
    return (1 / n) * sum([abs(y - y_hat) for y, y_hat in zip(Y, Y_hat)])


def get_mse(Y: List[float], Y_hat: List[float]) -> float:
    assert len(Y) == len(Y_hat)
    n = len(Y)
    return (1 / n) * sum([(y - y_hat) ** 2 for y, y_hat in zip(Y, Y_hat)])


def get_rmse(Y: List[float], Y_hat: List[float]) -> float:
    assert len(Y) == len(Y_hat)
    return math.sqrt(get_mse(Y, Y_hat))


LOSS_FUNCTIONS: Dict[str, Callable] = {"MAE": get_mae, "MSE": get_mse, "RMSE": get_rmse}


def regression_loss():
    num_samples = input("Input number of samples: ")
    if not num_samples.isnumeric():
        raise ValueError(f"num_samples {num_samples} must be number")
    num_samples = int(num_samples)

    loss_name = input(f"Input loss function( {'|'.join(LOSS_FUNCTIONS)} ): ")
    if loss_name not in LOSS_FUNCTIONS:

        raise ValueError(f"{loss_name} is not a valid loss function")

    loss_func = LOSS_FUNCTIONS[loss_name]
    gen_list = lambda n: [random.uniform(0, 10) for i in range(n)]
    for i in range(num_samples):
        Y, Y_hat = gen_list(1), gen_list(1)
        loss = loss_func(Y, Y_hat)
        print(
            f"loss name : {loss_name} , sample : {i} , pred : {Y[0]} , target : {Y_hat[0]} , loss : {loss}"
        )


if __name__ == "__main__":
    regression_loss()
