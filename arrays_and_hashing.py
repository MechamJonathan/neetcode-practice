
from typing import List


class ArraysAndHashing():
    def contains_duplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for num in nums:
            if num in mySet:
                return True
            else:
                mySet.add(num)
        return False
