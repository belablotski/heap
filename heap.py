import math

class Heap(object):
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        print(self.heap)
        self.visualize_tree()
        self._heapify_up(len(self.heap) - 1)
        print(self.heap)
        self.visualize_tree()
        print('-' * 20)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return result

    def peek(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def visualize_tree(self):
        if not self.heap:
            print("Heap is empty")
            return

        height = math.ceil(math.log2(len(self.heap) + 1))
        max_width = 2 ** (height - 1)
        index = 0

        for level in range(height):
            level_width = 2 ** level
            level_nodes = self.heap[index:index+level_width]
            index += level_width

            spaces = ' ' * (max_width // level_width)
            print(spaces.join(map(str, level_nodes)).center(max_width * 2))
            
if __name__ == "__main__":
    heap = Heap()
    elements = [5, 3, 4, 2, 1, 6, 3, 8]
    for element in elements:
        heap.insert(element)
    print("Heap elements:", heap.heap)

    for element in sorted(elements, reverse=True):
        heap_max = heap.extract_max()
        assert heap_max == element, f'{heap_max} != {element}'
