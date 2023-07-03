from typing import Any, Self



class Task:
    def __init__(self, data) -> None:
        self._data = data
        self._next = None

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, data) -> None:
        self._data = data

    @property
    def next(self) -> Self:
        return self._next

    @next.setter
    def next(self, next) -> None:
        self._next = next

    def __str__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self) -> None:
        self._head: Task | None = None
        self._size: int = 0
        self._tail: Task | None = None

    @property
    def head(self) -> Task | None:
        return self._head

    @head.setter
    def head(self, head) -> None:
        self._head = head

    @property
    def tail(self) -> Task | None:
        return self._tail

    @tail.setter
    def tail(self, tail) -> None:
        self._tail = tail

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        """returns a iterator of the linked list"""
        current_task = self.head

        while current_task is not None:
            yield current_task
            current_task = current_task.next

    def __str__(self) -> str:
        """Returns formatted string to account for contained strings"""
        return str([str(task.data) for task in self]).replace("'", "")

    def _is_invalid(*args) -> bool:
        """Checks against *args to validate input/deletion values are valid"""
        return any([arg is None for arg in args])

    def _increase_size(self) -> None:
        self._size += 1

    def _reduce_size(self) -> None:
        if self._size > 0:
            self._size -= 1

    def enqueue(self, *args) -> None:
        """Appends task(s) to current queue and increments the size"""
        for task in args:
            if self._is_invalid(task):
                continue

            new_task = Task(task)

            if self.head is None:
                self.head = new_task
                self.tail = new_task
                self._increase_size()
                continue

            self.tail.next = new_task
            self.tail = new_task
            self._increase_size()
        return

    def dequeue(self) -> Task:
        """Returns the head, and replaces head with the next value, decrementing size"""
        if self.head is None:
            return

        task = self.head
        self.head = self.head.next
        self._reduce_size()
        return task

