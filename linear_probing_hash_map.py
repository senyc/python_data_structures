from typing import List, Any, Self

Key = str | int

class FullHashException(BaseException):
    """Structure is full"""

class Item:
    def __init__(self, key: Key, value: Any) -> None:
        self._key: Key = key
        self._value: Any = value
        self._tombstone: bool = False

    @property
    def key(self) -> Key:
        return self._key

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        self._value = new_value

    def __str__(self) -> str:
        """Returns string formatted to account for strings being stored"""
        return str([self.key, self.value]).replace("'", "")

    def __eq__(self, item: Self | Key) -> bool:
        """This is inverted in python3 - no need for __ne__"""
        try:
            return self.key == item.key
        except AttributeError:
            return self.key == item


class MyHash:
    def __init__(self, size: int) -> None:
        self._data: List[Item] = [None] * size
        self._size: int = size
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def getIndex(self, key: Key) -> int:
        return hash(key) % self._size

    def _traverse(self, index: int) -> int:
        return (index + 1) % self._size

    def _is_empty(self, item: Item | None) -> bool:
        return item is None or item._tombstone

    def insert(self, key: Key, value: Any) -> None:
        if self._size == self._length:
            raise FullHashException

        index: int = self.getIndex(key)

        new_item = Item(key, value)

        while not self._is_empty(self._data[index]):
            if self._data[index] == key:
                self._data[index] = new_item
                return
            index = self._traverse(index)

        self._data[index] = new_item
        self._length += 1
        return

    def remove(self, key: Key) -> None:
        index: int = self.getIndex(key)

        while not self._is_empty(self._data[index]):
            if self._data[index] == key:
                self._data[index]._tombstone = True
                self._length -= 1
                return
            index = self._traverse(index)

    def __getitem__(self, key: Key) -> Any | None:
        index: int = self.getIndex(key)

        while not self._is_empty(self._data[index]):
            if self._data[index] == key:
                return self._data[index].value
            index = self._traverse(index)

    def __setitem__(self, key: Key, value: Any) -> None:
        index: int = self.getIndex(key)

        while not self._is_empty(self._data[index]):
            if self._data[index] == key:
                self._data[index].value = value
                return
            index = self._traverse(index)

