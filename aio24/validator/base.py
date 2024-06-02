import abc
import functools
from typing import Any, Callable

from aio24.exception import TypeExecption


def is_int(n: int) -> bool:
    if type(n) is int:
        return True
    return False


def is_float(n: float) -> bool:
    if type(n) is float:
        return True
    return False


class BaseInputValidator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _validate(self, v: Any, k=None, raise_exception=True):
        pass

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            functools.wraps(func)
            for arg in args:
                self._validate(arg)
            for k, v in kwargs.items():
                self._validate(v, k)
            return func(*args, **kwargs)

        return wrapper


class InputTypeValidator(BaseInputValidator):
    def __init__(self, input_type) -> None:
        super().__init__()
        assert input_type in [int, float]
        self._valid_type = input_type
        if input_type is int:
            self._validate_type = is_int
        if input_type is float:
            self._validate_type = is_float

    def _validate(self, v: Any, k=None, raise_exception=True):
        type_valid = self._validate_type(v)
        if type_valid:
            return
        if raise_exception:
            if k:
                raise TypeExecption(f"{k} must have type {self._valid_type} ")
            raise TypeExecption(f"{v} must have type {self._valid_type} ")


class PositiveInputValidator(BaseInputValidator):
    def __init__(self) -> None:
        super().__init__()

    def _validate(self, v: Any, k=None, raise_exception=True):
        input_valid = True if v > 0 else False
        if input_valid:
            return
        if raise_exception:
            if k:
                raise TypeExecption(f"{k} must be greater than zero")
            raise TypeExecption(f"{v} must be greater than zero")
