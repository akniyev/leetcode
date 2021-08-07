from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        d = deque()
        d.append(0)
        result = [nums[0]]

        for i in range(1, n):
            while d and d[0] < i - k + 1:
                d.popleft()
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            result.append(nums[d[0]])

        return result[k - 1:]


s = Solution()
print(s.maxSlidingWindow([9, 11], 2))

