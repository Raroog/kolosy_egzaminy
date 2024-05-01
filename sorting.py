import random


class Sorting:

    def __init__(self, array) -> None:
        self.array = array

    def selection_sort(self):
        comparisons = 0
        swaps = 0
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                comparisons += 1
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            swaps += 1 if i != min_idx else 0
        print(f"Number of comparisons: {comparisons}, number of swaps: {swaps}")

    def insertion_sort(self):
        comparisons = 0
        swaps = 0
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                comparisons += 1
                self.array[j + 1] = self.array[j]
                swaps += 1
                j -= 1
            self.array[j + 1] = key
        print(f"Number of comparisons: {comparisons}, number of swaps: {swaps}")

    def compare(self, value_1, value_2):
        print(f"Difference between value_1 and value_2 is {abs(value_1 - value_2)}")


num_list =  [random.randint(0, 1000) for i in range(50)]
sorted_num_list = sorted(num_list)
reversed_num_list = sorted(num_list, reverse=True)

sorting = Sorting(num_list)
sorting_sorted = Sorting(sorted_num_list)
sorting_reversed = Sorting(reversed_num_list)

selection_sort(num_list)
selection_sort(sorted_num_list)
selection_sort(reversed_num_list)