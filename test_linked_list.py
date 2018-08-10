import unittest
from linked_list import Node

class TestNode(unittest.TestCase):

    def test(self):
        n1 = Node('hello')
        n2 = Node('world')
        n1.next = n2
        self.assertTrue(n1.next.val == 'world')

if __name__ == '__main__':
    unittest.main()
