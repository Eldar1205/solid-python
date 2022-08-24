from abc import ABC, abstractmethod
from typing import Generic, Iterable, Iterator, Sized, TypeVar

_TItem = TypeVar("_TItem")

# Represents a set - items are unique, and when iterated return by order of insertion
class ISet(ABC, Iterable[_TItem], Sized, Generic[_TItem]):
    @abstractmethod
    def add(self, item: _TItem) -> None:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[_TItem]:
        ...

# Problem: Adding an item isn't idempotent, 
# in contrast to set semantics. 
# In particular, after adding the same item twice 
# the len() will be 2 instead of 1.
class BadSet(ISet[_TItem], Generic[_TItem]):
    def __init__(self) -> None:
        self.__items_list = list[_TItem]()

    def add(self, item: _TItem) -> None:
        self.__items_list.append(item)

    def __len__(self) -> int:
        return len(self.__items_list)

    def __iter__(self) -> Iterator[_TItem]:
        return iter(self.__items_list)