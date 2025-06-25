
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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]: # the i > 0 is so we can safely check the next part of the conditional.
                                           # so we don't compare nums[-1] (the last number) by accident
                continue
                
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum == 0:
                    result.append([n, nums[l], nums[r]]) # found a triplet! Add it to the result
                    # We are looking for multiple solutions in this problem, so move the pointers so we can continue
                    l += 1
                    r -= 1
                    # This is the duplicate-skip logic for the left pointer. After incrementing
                    # l, we could encounter the exact same number, which would just add the same 
                    # triplet. 
                    # First we check if nums[l] is equal to the num before it.
                    # checking l<r confirms their is still nums to view, otherwise we've done them
                    # all and need to move on
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
                elif threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                    
        return result
    
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res

