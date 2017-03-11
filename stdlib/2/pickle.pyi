# Stubs for pickle (Python 2)

from typing import Any, IO


HIGHEST_PROTOCOL = ...  # type: int


def dump(obj: Any, file: IO[str], protocol: int = None) -> None: ...
def dumps(obj: Any, protocol: int = ...) -> bytes: ...
def load(file: IO[str]) -> Any: ...
def loads(string: bytes) -> Any: ...


class PickleError(Exception):
    pass


class PicklingError(PickleError):
    pass


class UnpicklingError(PickleError):
    pass


class Pickler:
    def __init__(self, file: IO[str], protocol: int = None) -> None: ...

    def dump(self, obj: Any) -> None: ...

    def clear_memo(self) -> None: ...


class Unpickler:
    def __init__(self, file: IO[str]) -> None: ...

    def load(self) -> Any: ...
