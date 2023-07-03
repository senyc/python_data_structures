import unittest

from singly_linked_list import SLinkedList

class TestSLinkedList(unittest.TestCase):
    def test_append(self):
        """Tests the append method"""
        linked_list = SLinkedList()
        linked_list.append(1, 2, 3, 4, 5)

        self.assertEqual(len(linked_list), 5)
        linked_list.append(None)
        self.assertEqual(len(linked_list), 5)
        linked_list.append("Frank")
        self.assertEqual(len(linked_list), 6)
        linked_list.append("John", 4, None)
        self.assertEqual(len(linked_list), 8)
        linked_list.append("Tom", None, None)
        self.assertEqual(len(linked_list), 9)
        linked_list.append(44434343443, None, 3)
        self.assertEqual(len(linked_list), 11)

    def test_length(self):
        """Tests the length method"""
        linked_list_one = SLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        self.assertEqual(len(linked_list_one), 5)

        linked_list_two = SLinkedList()
        self.assertEqual(len(linked_list_two), 0)

        linked_list_three = SLinkedList()
        linked_list_three.append("Frank", "ted", None)
        self.assertEqual(len(linked_list_three), 2)

    def test_delete(self):
        """Tests the delete method"""
        linked_list = SLinkedList()
        linked_list.append(1, 2, 3, 4, 5)

        self.assertEqual(len(linked_list), 5)
        linked_list.delete(5)
        self.assertEqual(len(linked_list), 4)
        linked_list.delete(None)
        self.assertEqual(len(linked_list), 4)
        linked_list.delete(6)
        self.assertEqual(len(linked_list), 4)
        linked_list.delete(1)
        self.assertEqual(len(linked_list), 3)
        self.assertEqual(str(linked_list), '[2, 3, 4]')

    def test_delete_head(self):
        linked_list = SLinkedList()
        linked_list.append(1)
        self.assertEqual(len(linked_list), 1)
        linked_list.delete(1)
        self.assertEqual(len(linked_list), 0)

    def test_str(self):
        """Tests the string method"""
        linked_list_one = SLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        self.assertEqual(str(linked_list_one), "[1, 2, 3, 4, 5]")

        linked_list_two = SLinkedList()
        linked_list_two.append("1,2,3,4,5", "frank", "None", 1)
        self.assertEqual(str(linked_list_two), "['1,2,3,4,5', 'frank', 'None', 1]")

    def test_insert_before(self):
        """Tests the insert_before method"""
        linked_list_one = SLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        linked_list_one.insert_before(2, 0)
        self.assertEqual(str(linked_list_one), "[1, 0, 2, 3, 4, 5]")
        linked_list_one.insert_before(1, "frank")
        self.assertEqual(str(linked_list_one), "['frank', 1, 0, 2, 3, 4, 5]")

        linked_list_two = SLinkedList()
        linked_list_two.append()
        linked_list_two.insert_before(3, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(None, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(2, None)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(444, 26)
        self.assertEqual(str(linked_list_two), "[2, 26]")

    def test_insert_after(self):
        """Tests the insert_after method"""
        linked_list_one = SLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        linked_list_one.insert_after(2, 0)
        self.assertEqual(str(linked_list_one), "[1, 2, 0, 3, 4, 5]")
        linked_list_one.insert_after(1, "frank")
        self.assertEqual(str(linked_list_one), "[1, 'frank', 2, 0, 3, 4, 5]")
        linked_list_one.insert_after("Idontexist", "john")
        self.assertEqual(str(linked_list_one), "[1, 'frank', 2, 0, 3, 4, 5, 'john']")

        linked_list_two = SLinkedList()
        linked_list_two.append()
        linked_list_two.insert_before(3, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(None, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(2, None)
        self.assertEqual(str(linked_list_two), "[2]")

    def test_prepend(self):
        linked_list = SLinkedList()
        self.assertTrue(len(linked_list) == 0)
        linked_list.prepend(1)
        self.assertTrue(len(linked_list) == 1)
        self.assertTrue(str(linked_list) == '[1]')
        linked_list.prepend(2)
        self.assertTrue(len(linked_list) == 2)
        self.assertTrue(str(linked_list) == '[2, 1]')
        linked_list.delete(2)
        self.assertTrue(len(linked_list) == 1)
        self.assertTrue(str(linked_list) == '[1]')
        linked_list.delete(1)
        self.assertTrue(len(linked_list) == 0)
        linked_list.prepend(1, 2, 3)
        self.assertEqual(str(linked_list), '[3, 2, 1]')


if __name__ == '__main__':
    unittest.main()
