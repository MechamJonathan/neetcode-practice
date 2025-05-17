
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
    
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(countS) != len(countT):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        if countS != countT:
            return False
        return True
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNums = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in previousNums:
                return [previousNums[diff], i]
            else:
                previousNums[n] = i
