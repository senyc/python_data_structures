import unittest
from singly_linked_list import SLinkedList

class TestSLinkedList(unittest.TestCase):
    
    def test_append(self):
        """Tests the append method"""
        
        linked_list = SLinkedList()
        linked_list.append(1,2,3,4,5)
        
        self.assertEqual(len(linked_list), 5)
        self.assertEqual(len(linked_list.append(None)), 5)
        self.assertEqual(len(linked_list.append("Frank")), 6)
        self.assertEqual(len(linked_list.append("John",4, None)), 8)
        self.assertEqual(len(linked_list.append("Tom",None, None)), 9)
        self.assertEqual(len(linked_list.append(44434343443 ,None, 3)), 11)
        
    def test_length(self):
        """Tests the length method"""
        
        linked_list_one = SLinkedList()
        linked_list_one.append(1,2,3,4,5)
        self.assertEqual(len(linked_list_one), 5)
        
        linked_list_two = SLinkedList()
        self.assertEqual(len(linked_list_two), 0)
        
        linked_list_three = SLinkedList()
        linked_list_three.append("Frank", "ted", None)
        self.assertEqual(len(linked_list_three), 2)
        
    def test_delete(self):
        """Tests the delete method"""
        
        linked_list = SLinkedList()
        linked_list.append(1,2,3,4,5)
        self.assertEqual(len(linked_list), 5)
        self.assertEqual(len(linked_list.delete(5)), 4)
        self.assertEqual(len(linked_list.delete(None)),4)
        self.assertEqual(len(linked_list.delete(6)),4)
        self.assertEqual(len(linked_list.delete(1)),3)
        
    def test_str(self):
        """Tests the string method"""
        
        linked_list_one = SLinkedList()
        linked_list_one.append(1,2,3,4,5)
        self.assertEqual(str(linked_list_one), "[1, 2, 3, 4, 5]")
        
        linked_list_two = SLinkedList()
        linked_list_two.append("1,2,3,4,5", "frank", "None", 1)
        self.assertEqual(str(linked_list_two), "['1,2,3,4,5', 'frank', 'None', 1]")
        
        
    def test_insert_before(self):
        """Tests the insert_before method"""
        
        linked_list_one = SLinkedList()
        linked_list_one.append(1,2,3,4,5)
        self.assertEqual(str(linked_list_one.insert_before(2,0)), "[1, 0, 2, 3, 4, 5]")
        self.assertEqual(str(linked_list_one.insert_before(1,"frank")), "['frank', 1, 0, 2, 3, 4, 5]")
        
        linked_list_two = SLinkedList()
        linked_list_two.append()
        self.assertEqual(str(linked_list_two.insert_before(3, 2)), "[2]")
        self.assertEqual(str(linked_list_two.insert_before(None, 2)), "[2]")
        self.assertEqual(str(linked_list_two.insert_before(2, None)), "[2]")
        self.assertEqual(str(linked_list_two.insert_before(444, 26)), "[2, 26]")
        
        
        
    def test_insert_after(self):
        """Tests the insert_after method"""
        
        linked_list_one = SLinkedList()
        linked_list_one.append(1,2,3,4,5)
        self.assertEqual(str(linked_list_one.insert_after(2, 0)), "[1, 2, 0, 3, 4, 5]")
        self.assertEqual(str(linked_list_one.insert_after(1, "frank")), "[1, 'frank', 2, 0, 3, 4, 5]")
        self.assertEqual(str(linked_list_one.insert_after("Idontexist", "john")), "[1, 'frank', 2, 0, 3, 4, 5, 'john']")
        
        
        linked_list_two = SLinkedList()
        linked_list_two.append()
        self.assertEqual(str(linked_list_two.insert_before(3, 2)), "[2]")
        self.assertEqual(str(linked_list_two.insert_before(None, 2)), "[2]")
        self.assertEqual(str(linked_list_two.insert_before(2, None)), "[2]")
        
        
        
if __name__ == '__main__':
    unittest.main()        
