
from typing import List


class BinarySearch():
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            median = (low + high) // 2

            if nums[median] == target:
                return median
            elif nums[median] < target:
                low = median + 1
            else:
                high = median - 1
        return -1
    
    #Search Matrix
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False
    
    def binary_search(self, row, target):
        low, high = 0, len(row) - 1

        while low <= high:
            median = (low + high) // 2

            if row[median] == target:
                return True
            elif row[median] < target:
                low = median + 1
            else:
                high = median - 1
        return False
        