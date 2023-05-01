from typing import TypeVar, Iterable, Callable

X = TypeVar("X")
Y = TypeVar("Y")


def map_(f: Callable[[X], Y], xs: Iterable[X]) -> Iterable[Y]:
    for x in xs:
        yield f(x)