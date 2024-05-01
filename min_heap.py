class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def remove(self, value):
        if value in self.heap:
            index = self.heap.index(value)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self.heapify_down(index)

    def heapify_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def find_with_trace(self, value):
        visited = []
        for i, val in enumerate(self.heap):
            visited.append(val)
            if val == value:
                return True, visited
        return False, visited

    def __str__(self):
        return str(self.heap)

# Przypadek użycia
heap = MinHeap()

# Wstawianie elementów
elements = [15, 40, 30, 50, 10, 100, 40]
for e in elements:
    heap.insert(e)

# Sprawdzanie obecności 40 i drukowanie odwiedzonych elementów
found, visited = heap.find_with_trace(40)
print("Czy 40 jest w kopcu:", found)
print("Odwiedzone elementy przed znalezieniem 40:", visited)

# Usuwanie elementu 10
heap.remove(10)
print("Kopiec po usunięciu elementu 10:", heap)
