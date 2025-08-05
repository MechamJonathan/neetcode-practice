
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
        