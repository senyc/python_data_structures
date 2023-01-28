def invalid_data(*args):
    """
    Checks against *args to validate input/deletion values are valid

    :return: Returns true if values are invalid
    :rtype: bool
    """
    
    for arg in args:
        if arg is None:
            return True
    return False


class Node():
    def __init__(self, data):
        """
        Takes in value to set :attr: `_data`

        :param data: value to be set for node  
        :type data: Any
        """

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
    def next(self,next):
        self._next = next
        
    def __str__(self):
        return str(self.data)


class SLinkedList():
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
        """
        Generator to be used as iterator, this doesn't seem to 
        fully follow standards (no `__next__`), but for now this is fine

        :current_node: current node from self.head -> end  
        :rtype: :class: `Node`
        """
        
        current_node = self.head
        
        while current_node is not None:
            yield current_node
            current_node = current_node.next
              
    def __str__(self):
        """
        Allows for the printing of the data structure

        :return: String of list
        :rtype: string
        """
        
        elements = []
        
        for current_node in self:
            elements.append(current_node.data)
        return str(elements)
            
    def __len__(self):
        """
        Counts nodes and returns number
        Compatible with len() 
        
        :return: length of nodes
        :rtype: int
        """
        
        length = 0

        for _ in self: length += 1

        return length
            
    def append(self, *args):
        """
        Takes in variable inputs (nonstandard but fun)
        and adds to the end of the list
        
        :return: Returns the object
        :rtype: :class: `SLinkedList`
        """
        
        for arg in args:
            if invalid_data(arg):
                continue
            
            new_node = Node(arg)
            
            if self.head is None:
                self.head = new_node
                continue
            
            # Iterates through all of the current values
            for current_node in self: continue
            
            current_node.next = new_node

        return self

    def insert_before(self, existing_data, new_data):
        """
        Inserts node with :param: `new_data` 
        before :param: `existing_data`
        
        :param existing_data: Data searched for
        :type existing_data: Object
        :param new_data: Data that is inserted
        :type new_data: Object
        :return: Returns the object
        :rtype: :class: `SLinkedList`
        """
        
        if invalid_data(existing_data, new_data):
            return self
        
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return self    

        # If head node has `existing_data` make `new_node` head
        if self.head.data is existing_data:
            new_node.next = self.head
            self.head = new_node
            return self
        
        previous_node = self.head # Needed as we don't have `.prev`
        
        for current_node in self:
            if current_node.data is existing_data:
                new_node.next = current_node
                previous_node.next = new_node
                return self
            
            previous_node = current_node

        # Appends `new_node` if `existing_value` not found
        current_node.next = new_node
        return self
        
    def insert_after(self, existing_data, new_data):
        """
        Inserts node with :param: `new_data`
        after :param: `existing_data`

        :param existing_data: Data that is searched for
        :type existing_data: Object
        :param new_data: Data that is inserted
        :type new_data: Object
        :return: Returns the object
        :rtype: :class: `SLinkedList`
        """
        
        if invalid_data(existing_data, new_data):
            return self
        
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return self    
        
        for current_node in self:
            if current_node.data is existing_data:

                # Logic based on if `existing_data` is tail node 
                if current_node.next is None:
                    current_node.next = new_node
                    return self
                
                # Logic if value is surrounded by others in list
                new_node.next = current_node.next
                current_node.next = new_node
                return self

        # Appends `new_node` if `existing_value` not found
        current_node.next = new_node
        return self
        
    def delete(self, unwanted_value):
        """
        Removal of node with inputted data

        :param data: Data that is searched for and deleted
        :type data: Object
        :return: Returns the object
        :rtype: :class: `SLinkedList`
        """
        
        if invalid_data(unwanted_value) or self.head is None:
            return self
        
        previous_node = self.head
        
        for current_node in self:
            if current_node.data is unwanted_value:
                
                # Logic based on if unwanted value is tail node
                if current_node.next is None:
                    previous_node.next = None
                    return self

                # Logic based on if unwanted value is head node
                if current_node is self.head:
                    self.head = self.head.next
                    return self
                
                # Logic if value is surrounded by others in list
                previous_node.next = current_node.next
                return self

            previous_node = current_node
            
        # Returns object if not found
        return self
