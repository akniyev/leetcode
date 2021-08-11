from typing import *


class Solution:
    def binary_find_first(self, nums, target):
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                j = m
            elif nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        if nums[i] == target:
            return i
        else:
            return -1

    def binary_find_last(self, nums, target):
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j + 1) // 2
            if nums[m] == target:
                i = m
            elif nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        if nums[j] == target:
            return i
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        return [self.binary_find_first(nums, target), self.binary_find_last(nums, target)]


s = Solution()
print(s.searchRange([2, 2], 2))