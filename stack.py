def invalid(*args):
    """
    Checks against *args to validate input/deletion values are valid

    :return: Returns true if values are invalid
    :rtype: bool
    """
    
    for arg in args:
        if arg is None:
            return True
    return False


class Item():
    def __init__(self, data):
        self._data = data
        self._next = None
            
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
        
    def __str__(self):
        return str(self.data)
    
class Stack():    
    def __init__(self):
        self._head = None
    
    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head):
        self._head = head

    def __iter__(self):
        """
        Generator to be used as iterator, this doesn't seem to 
        fully follow standards (no `__next__`), but for now this is fine

        :current_node: current node from self.head -> end  
        :rtype: :class: `Node`
        """
        
        current_value = self.head
        
        while current_value is not None:
            yield current_value
            current_value = current_value.next
            
    def __str__(self):
        """
        Allows for the printing of the data structure

        :return: String of stack
        :rtype: string
        """
        
        return str([item.data for item in self ])
        
    def __len__(self):
        """
        Counts items and returns number-
        Compatible with len() 
        
        :return: number of nodes
        :rtype: int
        """

        length = 0
        for _ in self: length += 1
        return length

    def pop(self):
        """
        Sets new `head` and returns previous `head`

        :return: previous top item
        :rtype: :class: `Item`
        """
        
        if self.head is None:
            return None
        
        top = self.head
        
        self.head = self.head.next
        
        return top
    
    def push(self, *args):
        """
        pushes any amount of values to the top of the stack

        :param args: any amount of values to be pushed 
        :type args: any
        :return: object for method-chaining
        :rtype: :class: `Stack`
        """

        for arg in args:
            if invalid(arg):
                continue

            new_top = Item(arg)
            
            new_top.next = self.head
            self.head = new_top
            
        return self
