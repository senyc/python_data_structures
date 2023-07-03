from typing import Any, Self



class Item():
    def __init__(self, data) -> None:
        self._data: Any = data
        self._next: Self | None = None

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, data) -> Self | None:
        self._data = data

    @property
    def next(self) -> Self | None:
        return self._next

    @next.setter
    def next(self, next) -> None:
        self._next = next

    def __str__(self) -> str:
        return str(self.data)

class Stack():
    def __init__(self) -> None:
        self._head = None
        self._size: int = 0

    @property
    def head(self) -> Item | None:
        return self._head

    @head.setter
    def head(self, head) -> None:
        self._head = head

    def __iter__(self):
        """returns a iterator of the linked list"""
        current_value = self.head

        while current_value is not None:
            yield current_value
            current_value = current_value.next

    def __str__(self) -> str:
        """Returns formatted string to account for contained strings"""
        return str([item.data for item in self]).replace("'", "")

    def __len__(self) -> int:
        return self._size

    def _is_invalid(*args) -> bool:
        """Checks against *args to validate input/deletion values are valid"""
        return any([arg is None for arg in args])

    def pop(self) -> Item | None:
        """Sets new `head` and returns previous `head`"""
        if self.head is None:
            return None

        top = self.head
        self.head = self.head.next
        self._size -= 1
        return top

    def push(self, *args) -> None:
        """Pushes any amount of values to the top of the stack"""
        for arg in args:
            if self._is_invalid(arg):
                continue

            new_top = Item(arg)

            new_top.next = self.head
            self.head = new_top
            self._size += 1

