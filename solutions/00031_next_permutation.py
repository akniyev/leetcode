from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            nums.sort()
            return

        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        tail_start = i + 1
        for i in range(tail_start, n - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        i = tail_start
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


s = Solution()
nums = [1, 5, 1]
s.nextPermutation(nums)
print(nums)