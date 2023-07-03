from typing import List, Any, Self

from singly_linked_list import SLinkedList

Key = str | int

class Item:
    def __init__(self, key: Key, value: Any) -> None:
        self._key: Key = key
        self._value: Any = value

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
        return str([self.key, self.value]).replace("'", "")

    def __eq__(self, item: Self | Key) -> bool:
        try:
            return self.key == item.key
        except AttributeError:
            return self.key == item


class MyHash:
    def __init__(self, size: int) -> None:
        self._data: List[SLinkedList[Item]] = [None] * size
        self._size: int = size
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def _getIndex(self, key: Key) -> int:
        return hash(key) % self._size

    def insert(self, key: Key, value: Any) -> None:
        index: int = self._getIndex(key)

        new_item = Item(key, value)

        if self._data[index] is None:
            self._data[index] = SLinkedList()
            self._data[index].prepend(new_item)
            self._length += 1
            return

        for item in self._data[index]:
            if item.data == key:
                item.data.value = value
                return

        self._data[index].prepend(new_item)
        self._length += 1

    def remove(self, key: Key) -> None:
        index: int = self._getIndex(key)

        if self._data[index] is None:
            return

        for item in self._data[index]:
            if item.data == key:
                deletion_node = item.data

        self._data[index].delete(deletion_node)
        self._length -= 1

    def __getitem__(self, key: Key) -> Any:
        index: int = self._getIndex(key)

        for item in self._data[index]:
            if item.data == key:
                return item.data.value

    def __setitem__(self, key: Key, value: Any) -> None:
        index: int = self._getIndex(key)

        for item in self._data[index]:
            if item.data == key:
                item.data.value = value

