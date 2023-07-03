import unittest

from my_hash import MyHash
from my_hash import Item

class TestItem(unittest.TestCase):

    def test_equal(self):
        item_one = Item(1, 'test')
        item_one_eq = Item(1, 'test')
        item_two = Item(2, 'test2')
        item_two_eq = Item(2, 'test2')

        self.assertNotEqual(item_one, item_two)
        self.assertEqual(item_one, item_one)
        self.assertEqual(item_one, item_one_eq)
        self.assertEqual(item_two, item_two_eq)

    def test_string(self):
        item_one = Item(1, 'test')
        item_two = Item(2, 'test2')

        self.assertNotEqual(str(item_one), '[2, test2]')
        self.assertEqual(str(item_one), '[1, test]')
        self.assertEqual(str(item_two), '[2, test2]')

class TestMyHash(unittest.TestCase):

    def test_insert(self):
        """Tests the inserting into a hash map"""
        my_hash = MyHash(15)

        my_hash.insert(1, 'frank')
        self.assertEqual(len(my_hash), 1)
        self.assertEqual(my_hash[1], 'frank')

        my_hash.insert(2, 'frank2')
        self.assertEqual(my_hash[2], 'frank2')
        self.assertEqual(len(my_hash), 2)

        my_hash.insert(552, 'frank3')
        self.assertEqual(my_hash[552], 'frank3')
        self.assertEqual(len(my_hash), 3)

        # Inserting at the same key should replace the value
        my_hash.insert(1, 'frank4')
        self.assertEqual(my_hash[1], 'frank4')
        self.assertEqual(len(my_hash), 3)

    def test_insert_one_bucket(self):
        """Tests the insertion into a single bucket"""
        my_hash = MyHash(100)
        self.assertTrue(len(my_hash) == 0)
        my_hash.insert(1, 'frank')
        my_hash.insert(11, 'frank2')
        my_hash.insert(2, 'frank')
        my_hash.insert(3, 'frank')
        my_hash.insert(4, 'frank')
        my_hash.insert(5, 'frank')
        my_hash.insert(6, 'frank')
        my_hash.insert(7, 'frank')
        self.assertTrue(len(my_hash) == 8)
        my_hash.insert(8, 12312)
        self.assertTrue(len(my_hash) == 9)

    def test_remove(self):
        """Tests the removal of nodes"""
        my_hash = MyHash(16)

        my_hash.insert(1, 'frank1')
        my_hash.insert(11, 'frank11')
        my_hash.insert(2, 'frank2')
        my_hash.insert(3, 'frank3')
        my_hash.insert(4, 'frank4')
        my_hash.insert(5, 'frank5')
        my_hash.insert(6, 'frank6')
        my_hash.insert(7, 'frank7')

        self.assertEqual(len(my_hash), 8)

        my_hash.remove(7)
        self.assertEqual(len(my_hash), 7)
        self.assertNotEqual(my_hash[7], 'frank7')

        my_hash.remove(11)
        self.assertNotEqual(my_hash[11], 'frank11')

    def test_remove_one_bucket(self):
        """Tests the removal of nodes"""
        my_hash = MyHash(19)

        my_hash.insert(1, 'frank1')
        my_hash.insert(11, 'frank11')
        my_hash.insert(2, 'frank2')
        my_hash.insert(3, 'frank3')
        my_hash.insert(4, 'frank4')
        my_hash.insert(5, 'frank5')
        my_hash.insert(6, 'frank6')
        my_hash.insert(7, 'frank7')

        self.assertEqual(len(my_hash), 8)

        my_hash.remove(7)
        self.assertEqual(len(my_hash), 7)
        self.assertNotEqual(my_hash[7], 'frank7')

        my_hash.remove(11)
        self.assertNotEqual(my_hash[11], 'frank11')
        my_hash.remove(1)
        self.assertEqual(len(my_hash), 5)
        self.assertFalse(my_hash[1] == 'frank1')
        my_hash.insert(1, 'frank1')
        self.assertTrue(my_hash[1] == 'frank1')


if __name__ == '__main__':
    unittest.main()
