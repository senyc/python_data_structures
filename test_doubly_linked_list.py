import unittest

from doubly_linked_list import DLinkedList

class TestDLinkedList(unittest.TestCase):
    def test_append(self):
        """Tests the append method"""
        linked_list = DLinkedList()
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
        linked_list.append(44443443, None, 3)
        self.assertEqual(len(linked_list), 11)

    def test_length(self):
        """Tests the length method"""
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        self.assertEqual(len(linked_list_one), 5)

        linked_list_two = DLinkedList()
        self.assertEqual(len(linked_list_two), 0)

        linked_list_three = DLinkedList()
        linked_list_three.append("Frank", "ted", None)
        self.assertEqual(len(linked_list_three), 2)

    def test_delete(self):
        """Tests the delete method"""
        linked_list = DLinkedList()
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

    def test_delete_head(self):
        """Tests the removal of the head node"""
        linked_list = DLinkedList()
        linked_list.append(1, 2, 3, 4, 5)
        self.assertEqual(len(linked_list), 5)
        linked_list.delete(1)
        self.assertEqual(len(linked_list), 4)
        linked_list.delete(None)
        self.assertEqual(len(linked_list), 4)
        linked_list.delete(6)
        self.assertEqual(len(linked_list), 4)

    def test_str(self):
        """Tests the string method"""
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        self.assertEqual(str(linked_list_one), "[1, 2, 3, 4, 5]")

        linked_list_two = DLinkedList()
        linked_list_two.append("1,2,3,4,5", "frank", "None", 1)
        self.assertEqual(str(linked_list_two), "['1,2,3,4,5', 'frank', 'None', 1]")

    def test_insert_before(self):
        """Tests the insert_before method"""
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        linked_list_one.insert_before(2, 0)
        self.assertEqual(str(linked_list_one), "[1, 0, 2, 3, 4, 5]")
        linked_list_one.insert_before(1, "frank")
        self.assertEqual(str(linked_list_one), "['frank', 1, 0, 2, 3, 4, 5]")

        linked_list_two = DLinkedList()
        linked_list_two.append()
        linked_list_two.insert_before(3, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(None, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(2, None)
        self.assertEqual(str(linked_list_two), "[2]")

    def test_insert_after(self):
        """Tests the insert_after method"""
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        linked_list_one.insert_after(2, 0)
        self.assertEqual(str(linked_list_one), "[1, 2, 0, 3, 4, 5]")
        linked_list_one.insert_after(1, "frank")
        self.assertEqual(str(linked_list_one), "[1, 'frank', 2, 0, 3, 4, 5]")

        linked_list_two = DLinkedList()
        linked_list_two.append()
        linked_list_two.insert_before(3, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(None, 2)
        self.assertEqual(str(linked_list_two), "[2]")
        linked_list_two.insert_before(2, None)
        self.assertEqual(str(linked_list_two), "[2]")

    # @unittest.skip("skip")
    def test_reverse(self):
        "Tests the reverse method"

        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        linked_list_one.reverse()
        self.assertEqual(5, len(linked_list_one))
        self.assertEqual("[5, 4, 3, 2, 1]", str(linked_list_one))

        linked_list_two = DLinkedList()
        linked_list_two.append(1, 2, 3, 4, 5)
        linked_list_two.delete(2)
        linked_list_two.reverse()
        self.assertEqual(4, len(linked_list_two))
        self.assertEqual("[5, 4, 3, 1]", str(linked_list_two))

        linked_list_two.delete(5)
        linked_list_two.reverse()
        self.assertEqual("[1, 3, 4]", str(linked_list_two))
        linked_list_two.reverse()
        self.assertEqual("[4, 3, 1]", str(linked_list_two))

    def test_get_prev(self):
        "Tests the get_prev method"
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)

        prev_value = linked_list_one.get_prev(2)
        self.assertEqual("1", str(prev_value))
        prev_value = linked_list_one.get_prev(5)
        self.assertEqual("4", str(prev_value))
        prev_value = linked_list_one.get_prev(6)
        self.assertEqual("None", str(prev_value))
        prev_value = linked_list_one.get_prev(None)
        self.assertEqual("None", str(prev_value))

    def test_get_next(self):
        "Tests the get_prev method"
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)

        next_value = linked_list_one.get_next(2)
        self.assertEqual("3", str(next_value))
        next_value = linked_list_one.get_next(3)
        self.assertEqual("4", str(next_value))
        next_value = linked_list_one.get_next(6)
        self.assertEqual("None", str(next_value))
        next_value = linked_list_one.get_next(None)
        self.assertEqual("None", str(next_value))
        next_value = linked_list_one.get_next(1)
        self.assertEqual("2", str(next_value))

    def test_standard_prev(self):
        """Validates that the `.prev` node function is functioning correctly"""
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        node = linked_list_one.get(5)
        self.assertEqual(node, 5)
        self.assertEqual(node.prev, 4)

    def test_delete_prev(self):
        """Validates that the `.prev` node function is functioning correctly"""
        linked_list_one = DLinkedList()
        linked_list_one.append(1, 2, 3, 4, 5)
        linked_list_one.delete(4)
        node = linked_list_one.get(5)
        self.assertEqual(node, 5)
        self.assertEqual(node.prev, 3)

        linked_list_one.delete(1)
        node = linked_list_one.get(3)
        self.assertEqual(node, 3)
        self.assertEqual(node.prev, 2)
        self.assertEqual(str(linked_list_one), '[2, 3, 5]')

        linked_list_one.delete(2)
        node = linked_list_one.get(3)
        self.assertEqual(node.prev, None)



if __name__ == '__main__':
    unittest.main()

