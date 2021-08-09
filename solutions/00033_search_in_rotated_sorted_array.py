from typing import *


def find_min(nums: List[int]) -> int:
    n = len(nums)
    if n < 2 or nums[0] < nums[-1]:
        return 0
    i = 1
    j = n - 1
    while i < j:
        m = (i + j) // 2
        if nums[m] < nums[m - 1]:
            return m

        if nums[m] < nums[0]:
            j = m - 1
        else:
            i = m + 1

    return (i + j) // 2


def binary_search(nums: List[int], start_i: int, start_j: int, value: int) -> Optional[int]:
    i = start_i
    j = start_j
    while i < j:
        m = (i + j) // 2
        if nums[m] == value:
            return m
        if nums[m] < value:
            i = m + 1
        else:
            j = m - 1
    m = (i + j) // 2
    if start_i <= m <= start_j and nums[m] == value:
        return m
    else:
        return None


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_index = find_min(nums)
        index_left = binary_search(nums, 0, min_index - 1, target)
        index_right = binary_search(nums, min_index, n - 1, target)
        if index_left is not None:
            return index_left
        if index_right is not None:
            return index_right
        return -1


s = Solution()
arr = [1, 2, 3]
shift = 1
arr = arr[shift:] + arr[:shift]
print(arr)
s.search(arr, 4)