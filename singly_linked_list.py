
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
    def __init__(self, data=None):
        """By default sets the data to None, and next to None"""

        self.data = data
        self.next = None


class SLinkedList():
    def __init__(self):
        self.head = Node()

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
            current_node = self.head

            # Iterates until end node is "in sight"
            while current_node.next is not None:
                current_node = current_node.next

            # Sets previously None value to new_node
            # This of course sets the last node to None
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
        current_node = self.head
        
        # Run until next is None or next data is `existing_data`
        while current_node.next is not None and current_node.next.data is not existing_data:
            current_node = current_node.next
        
        # Does not need to keep rest of values 
        # in sequence as nothing is after
        if current_node.next is None:
            current_node.next = new_node
            return self
        
        new_node.next = current_node.next
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
        current_node = self.head

        # Checks for null or current_node data is what is searched for
        while current_node is not None and current_node.data is not existing_data:
            previous_node = current_node # Saved value for later
            current_node = current_node.next
        
        # If no value after node input value at tail
        if current_node.next == None:
            current_node.next = new_node
            return self
            
        future_node = current_node.next
        current_node.next = new_node
        new_node.next = future_node
        current_node = previous_node
        return self
        
        
    def delete(self, data):
        """
        Removal of node with inputted data

        :param data: Data that is searched for and deleted
        :type data: Object
        :return: Returns the object
        :rtype: :class: `SLinkedList`
        """
        
        if invalid_data(data):
            return self
        
        current_node = self.head
        
        while current_node is not None and current_node.data is not data:
            previous_node = current_node
            current_node = current_node.next
        
        # Node not found, nothing happens
        if current_node == None:
            return self
        
        # Current node is effectively kicked off of the stream
        previous_node.next = current_node.next
        return self
            
    def __str__(self):
        """
        Allows for the printing of the data structure

        :return: String of list
        :rtype: string
        """
        
        elements = []
        current_node = self.head

        while current_node.next is not None:
            
            # Head node is skipped by changing current index preemptively
            current_node = current_node.next
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
        current_node = self.head

        # Iterates through list counting the amount
        # of nodes until == None (similar to above)
        while current_node.next is not None:
            length += 1
            current_node = current_node.next
        return length
