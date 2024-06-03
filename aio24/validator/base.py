import abc
import functools
from typing import Any, Callable

from aio24.exception import TypeExecption


class BaseInputValidator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _validate(self, *args, **kwargs):
        pass

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            functools.wraps(func)
            self._validate(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper


class InputTypeValidator(BaseInputValidator):
    def __init__(self, *input_types) -> None:
        super().__init__()
        self._valid_types = input_types

    def _validate(self, *args, **kwargs):
        arg_values = list(args) + list(kwargs.values())
        for t, v in zip(self._valid_types, arg_values):
            if not isinstance(v, t):
                raise TypeExecption(f"{v} must have type {t} ")


class PositiveInputValidator(BaseInputValidator):
    def __init__(self) -> None:
        super().__init__()

    def _validate(self, *args, **kwargs):
        arg_values = list(args) + list(kwargs.values())
        for v in arg_values:
            if v < 0:
                raise TypeExecption(f"{v} must be greater than zero")
