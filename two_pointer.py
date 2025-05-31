
from typing import List


class TwoPointer():
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum()).lower()

        l, r = 0, len(cleaned) - 1

        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def twoSumII(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            elif total > target:
                r -= 1
