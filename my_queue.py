def invalid(*args) -> bool:
    """Checks against *args to validate input/deletion values are valid"""
    
    for arg in args:
        if arg is None:
            return True
    return False

class Task:
    def __init__(self, data) -> None:
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
    
    
class Queue:
    def __init__(self) -> None:
        self._head = None
        self._size = 0
        self._tail = None
    
    @property 
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head):
        self._head = head
        
    @property 
    def tail(self):
        return self._tail
    
    @tail.setter
    def tail(self, tail):
        self._tail = tail
        
    def __len__(self):
        return self._size

    def __iter__(self):
        current_task = self.head
        
        while current_task is not None:
            yield current_task
            current_task = current_task.next
            
    def __str__(self):
        return str([task.data for task in self])
    
    def increase_size(self) -> None:
        self._size += 1

    def reduce_size(self) -> None:
        
        if self._size > 0:
            self._size -= 1
        
    def enqueue(self, *args) -> 'Queue':
        """Appends task(s) to current queue and increments the size"""
        
        for task in args:
            if invalid(task): continue
            
            new_task = Task(task)
            
            if self.head is None:
                self.head = new_task
                self.tail = new_task
                self.increase_size()
                continue
            
            self.tail.next = new_task
            self.tail = new_task
            self.increase_size()
            
        return self
    
    def dequeue(self) -> 'Task':
        """Returns the head, and replaces head with the next value, decrementing size"""

        if self.head is None: return None
        
        task = self.head
        self.head = self.head.next 
        self.reduce_size()
        return task    
