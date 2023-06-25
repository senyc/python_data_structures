def isInvalid(*args):
    """Checks against *args to validate input/deletion values are valid"""
    return any([arg is None for arg in args])

class Node():
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

    def __str__(self):
        return str(self.data)


class DLinkedList():
    def __init__(self):
        "Sets the :attr: `_head` to None by default"
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def __iter__(self):
        """Returns a iterator of the linked list"""
        current_node = self.head

        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __reversed__(self):
        """Generator to be used as reversal iterator"""
        current_node = self.head
        # Pretty slow until a tail variable is added
        for current_node in self:
            continue

        while current_node is not None:
            yield current_node
            current_node = current_node.prev

    def __str__(self):
        return str([node.data for node in self])

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def append(self, *args):
        """Takes in variable inputs and adds to the end of the list"""
        for arg in args:
            if isInvalid(arg):
                continue

            new_node = Node(arg)

            # If empty list, make `new_node` head
            if self.head is None:
                self.head = new_node
                continue

            # Iterates through all of the current values, to "catch us up to end"
            for current_node in self:
                continue

            current_node.next = new_node
            new_node.prev = current_node
        return self

    def insert_before(self, existing_data, new_data):
        """Inserts node with :param: `new_data` before :param: `existing_data`"""
        if isInvalid(existing_data, new_data):
            return self

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return self

        if self.head.data == existing_data:
            self.head.next.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return self

        for current_node in self:
            if current_node.data == existing_data:
                # Sets new_node next/prev then add node to the stream
                new_node.next = current_node
                new_node.prev = current_node.prev
                current_node.prev.next = new_node
                current_node.prev = new_data
                return self

        # Appends `new_node` if `existing_value` not found
        current_node.next = new_node
        new_node.prev = current_node
        return self

    def insert_after(self, existing_data, new_data):
        """Inserts node with :param: `new_data` after :param: `existing_data`"""
        if isInvalid(existing_data, new_data):
            return self

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return self

        for current_node in self:
            if current_node.data == existing_data:
                if current_node.next is not None:
                    # Sets `new_node` next/prev then add node to the stream
                    new_node.next = current_node.next
                    new_node.prev = current_node
                    current_node.next.prev = new_node
                    current_node.next = new_node
                    return self
                # Exits loop to append if `existing_data` is tail node
                break

        # Appends `new_node` if `existing_value` not found or it tail node
        current_node.next = new_node
        new_node.prev = current_node
        return self

    def delete(self, unwanted_value):
        """Removal of node with inputted data"""
        if isInvalid(unwanted_value) or self.head is None:
            return self

        for current_node in self:
            if current_node.data == unwanted_value:
                # Replaces head node if data is `unwanted_value`
                if current_node is self.head:
                    self.head = current_node.next
                # Points the pre-existing next node to value behind deleted node
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                # Points the pre-existing previous node to value ahead of deleted node
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                return self
        # Returns object if not found
        return self

    def get_prev(self, data):
        """Returns the node previous to the given `data` :param:"""
        if isInvalid(data):
            return None
        if self.head.data == data:
            return None
        for current_node in self:
            if current_node.data == data:
                return current_node.prev
        return None

    def get_next(self, data):
        """Returns the next node to the given `data` :param:"""
        if isInvalid(data):
            return None

        for current_node in self:
            if current_node.data == data:
                if current_node.next is not None:
                    return current_node.next
        return None

    def reverse(self):
        """Reverses all of the values in the :class: `DLinkedList`"""
        previous_node = None
        current_node = self.head

        while current_node is not None:
            # Flips values from head -> tail
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node
            current_node = current_node.prev
        # Flips head and tail
        if previous_node is not None:
            self.head = previous_node.prev
        return self

