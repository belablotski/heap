import unittest
from heap import Heap

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_insert(self):
        self.heap.insert(5)
        self.assertEqual(self.heap.heap, [5])
        self.heap.insert(3)
        self.assertEqual(self.heap.heap, [5, 3])
        self.heap.insert(4)
        self.assertEqual(self.heap.heap, [5, 3, 4])
        self.heap.insert(2)
        self.assertEqual(self.heap.heap, [5, 3, 4, 2])
        self.heap.insert(1)
        self.assertEqual(self.heap.heap, [5, 3, 4, 2, 1])
        self.heap.insert(6)
        self.assertEqual(self.heap.heap, [6, 3, 5, 2, 1, 4])
        self.heap.insert(3)
        self.assertEqual(self.heap.heap, [6, 3, 5, 2, 1, 4, 3])
        self.heap.insert(8)
        self.assertEqual(self.heap.heap, [8, 6, 5, 3, 1, 4, 3, 2])

    def test_extract_max(self):
        elements = [5, 3, 4, 2, 1, 6, 3, 8]
        for element in elements:
            self.heap.insert(element)
        self.assertEqual(self.heap.extract_max(), 8)
        self.assertEqual(self.heap.extract_max(), 6)
        self.assertEqual(self.heap.extract_max(), 5)
        self.assertEqual(self.heap.extract_max(), 4)
        self.assertEqual(self.heap.extract_max(), 3)
        self.assertEqual(self.heap.extract_max(), 3)
        self.assertEqual(self.heap.extract_max(), 2)
        self.assertEqual(self.heap.extract_max(), 1)
        self.assertIsNone(self.heap.extract_max())

    def test_peek(self):
        self.assertIsNone(self.heap.peek())
        self.heap.insert(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.insert(3)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.insert(8)
        self.assertEqual(self.heap.peek(), 8)

if __name__ == '__main__':
    unittest.main()