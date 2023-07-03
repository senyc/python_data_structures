from typing import Self, Any

class Node():
    def __init__(self, data):
        """Takes in value to set :attr: `_data`"""
        self._data: Any = data
        self._next: Self | None = None

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, data) -> Self:
        self._data = data

    @property
    def next(self) -> Self | None:
        return self._next

    @next.setter
    def next(self, next) -> None:
        self._next = next

    def __str__(self) -> str:
        return str(self.data)

    def __eq__(self, node) -> bool:
        try:
            return self.data == node.data
        except AttributeError:
            return self.data == node


class SLinkedList():
    def __init__(self):
        "Sets the :attr: `_head` to None by default"
        self._head: Node | None = None

    @property
    def head(self) -> Node | None:
        return self._head

    @head.setter
    def head(self, node) -> None:
        self._head = node

    def __iter__(self):
        """returns a iterator of the linked list"""
        current_node = self.head

        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __str__(self) -> str:
        return str([node.data for node in self])

    def __len__(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length

    def _is_invalid(*args) -> bool:
        """Checks against *args to validate input/deletion values are valid"""
        return any([arg is None for arg in args])

    def append(self, *args) -> None:
        """Takes in variable inputs and adds to the end of the list"""
        for arg in args:
            if self._is_invalid(arg):
                continue

            new_node = Node(arg)

            if self.head is None:
                self.head = new_node
                continue
            # Iterates through all of the current values
            for current_node in self:
                continue
            current_node.next = new_node
        return

    def prepend(self, *args) -> None:
        """Takes in variable inputs and adds each the start of the list"""
        for arg in args:
            if self._is_invalid(arg):
                continue

            new_node = Node(arg)

            if self.head is None:
                self.head = new_node
                continue

            new_node.next = self.head
            self.head = new_node
        return

    def insert_before(self, existing_data, new_data) -> None:
        """Inserts node with :param: `new_data` before :param: `existing_data`"""
        if self._is_invalid(existing_data, new_data):
            return

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        # If head node has `existing_data` make `new_node` head
        if self.head.data == existing_data:
            new_node.next = self.head
            self.head = new_node
            return
        previous_node = self.head

        for current_node in self:
            if current_node.data is existing_data:
                new_node.next = current_node
                previous_node.next = new_node
                return

            previous_node = current_node
        # Appends `new_node` if `existing_value` not found
        current_node.next = new_node
        return

    def insert_after(self, existing_data, new_data) -> None:
        """Inserts node with :param: `new_data` after :param: `existing_data`"""
        if self._is_invalid(existing_data, new_data):
            return

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        for current_node in self:
            if current_node.data == existing_data:
                # Logic based on if `existing_data` is tail node
                if current_node.next is None:
                    current_node.next = new_node
                    return

                # Logic if value is surrounded by others in list
                new_node.next = current_node.next
                current_node.next = new_node
                return
        # Appends `new_node` if `existing_value` not found
        current_node.next = new_node
        return

    def delete(self, unwanted_value) -> None:
        """Removal of node with inputted data"""
        if self._is_invalid(unwanted_value) or self.head is None:
            return

        previous_node = self.head

        for current_node in self:
            if current_node.data == unwanted_value:
                # Logic based on if unwanted value is head node
                if current_node is self.head:
                    self.head = self.head.next
                    return
                # Logic based on if unwanted value is tail node
                if current_node.next is None:
                    previous_node.next = None
                    return
                # Logic if value is surrounded by others in list
                previous_node.next = current_node.next
                return
            previous_node = current_node
        return

