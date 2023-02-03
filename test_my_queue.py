import unittest
from my_queue import Queue

class TestQueue(unittest.TestCase):
    
    def test_enqueue(self):
        "Tests the enqueue method"
        
        queue_one = Queue()
        self.assertEqual(len(queue_one), 0)
        queue_one.enqueue(1,2,3,4,5)
        self.assertEqual(len(queue_one), 5)
        queue_one.enqueue()
        self.assertEqual(len(queue_one), 5)
        queue_one.enqueue(None)
        self.assertEqual(len(queue_one), 5)
        
        queue_two = Queue()
        self.assertEqual(len(queue_two), 0)
        queue_two.enqueue("Frank")
        self.assertEqual(len(queue_two), 1)
        queue_two.enqueue()
        self.assertEqual(len(queue_two), 1)
        queue_two.enqueue(None)
        self.assertEqual(len(queue_two), 1)
        
        queue_three = Queue()
        self.assertEqual(str(queue_three), "[]")
        queue_three.enqueue(1,2,3,4,5)
        self.assertEqual(str(queue_three), "[1, 2, 3, 4, 5]")
        queue_three.enqueue()
        self.assertEqual(str(queue_three), "[1, 2, 3, 4, 5]")
        queue_three.enqueue(None)
        self.assertEqual(str(queue_three), "[1, 2, 3, 4, 5]")
        
    def test_dequeue(self):
        "Tests the dequeue method"
        
        queue_one = Queue()
        queue_one.enqueue(1,2,3,4,5)
        
        self.assertEqual(len(queue_one), 5)
        self.assertEqual(queue_one.dequeue().data, 1)
        self.assertEqual(len(queue_one), 4)
        self.assertEqual(queue_one.dequeue().data, 2)
        self.assertEqual(len(queue_one), 3)
        self.assertEqual(queue_one.dequeue().data, 3)
        self.assertEqual(len(queue_one), 2)
        self.assertEqual(queue_one.dequeue().data, 4)
        self.assertEqual(len(queue_one), 1)
        self.assertEqual(queue_one.dequeue().data, 5)
        self.assertEqual(len(queue_one), 0)
        self.assertEqual(queue_one.dequeue(), None)
        self.assertEqual(len(queue_one), 0)
        
if __name__ == '__main__':
    unittest.main()
