from typing import *


class Solution:
    def binary_search(self, arr, i, j, value):
        while i < j:
            m = (i + j) // 2
            if arr[m] == value:
                return m
            if arr[m] < value:
                i = m + 1
            else:
                j = m
        if arr[i] == value:
            return i
        else:
            return None

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        i = 0
        j = n - 1

        while nums[i] == nums[j] and i < j:
            i += 1

        start_index = i

        while i < j:
            m = (i + j) // 2
            if nums[m] >= nums[start_index]:
                i = m + 1
            else:
                j = m

        left_result = self.binary_search(nums, start_index, i - 1, target)
        right_result = self.binary_search(nums, i, n - 1, target)

        return (left_result is not None) or (right_result is not None)


s = Solution()
arr = [1, 3]
shift = 1
arr = arr[shift:] + arr[:shift]
print(arr)
print("arr len is ", len(arr))
print(s.search(arr, 1))
