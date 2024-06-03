import os
import sys

current_path = sys.path[0]
aio_path = current_path.rsplit(os.path.sep, 2)[0]
sys.path.append(aio_path)

from aio24.validator import InputTypeValidator, PositiveInputValidator
from aio24 import get_std_input


@InputTypeValidator(int)
@PositiveInputValidator()
def get_recall(*, tp: int, fp: int, fn: int) -> float:
    recall = tp / (tp + fp)
    return recall


@InputTypeValidator(int)
@PositiveInputValidator()
def get_precision(*, tp: int, fp: int, fn: int) -> float:
    precision = tp / (tp + fn)
    return precision


@InputTypeValidator(int)
@PositiveInputValidator()
def get_f1_score(*, tp: int, fp: int, fn: int) -> float:
    precision = get_precision(tp=tp, fp=fp, fn=fn)
    recall = get_recall(tp=tp, fp=fp, fn=fn)
    f1 = 2 * precision * recall / (precision + recall)
    return f1


def print_metrics(tp: int, fp: int, fn: int):
    kwargs = {"tp": tp, "fp": fp, "fn": fn}
    p, r, f1 = get_precision(**kwargs), get_recall(**kwargs), get_f1_score(**kwargs)
    print(f"precision is {p}")
    print(f"recall is {r}")
    print(f"f1-score is {f1}")


if __name__ == "__main__":
    tp = get_std_input("tp = ", int)
    fp = get_std_input("fp = ", int)
    fn = get_std_input("fn = ", int)
    print_metrics(tp=tp, fp=fp, fn=fn)
