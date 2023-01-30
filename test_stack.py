import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    
    def test_push(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        
        stack.push(4)
        stack.push(3)
        stack.push(2)
        stack.push(1)
        self.assertEqual(len(stack), 4)
        
        stack.push(1)
        self.assertEqual(len(stack), 5)

    def test_pop(self):
        stack_one = Stack()
        stack_one.push(1, 2, 3, 4, 5, 6, 7)

        self.assertEqual(len(stack_one), 7)
        stack_one.pop()
        self.assertEqual(len(stack_one), 6)
        stack_one.pop()
        stack_one.pop()
        self.assertEqual(len(stack_one), 4)

        stack_two = Stack()
        stack_two.push(1, 2, 3, 4, 5, 6, 100)

        self.assertEqual(str(stack_two.pop()), '100')
        stack_two.pop()
        self.assertEqual(str(stack_two.pop()), '5')

        stack_three = Stack()

        self.assertEqual(stack_three.pop(), None)
        
if __name__ == '__main__':
    unittest.main()
