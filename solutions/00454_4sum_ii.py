from typing import *


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)

        sum_counts1 = dict()
        sum_counts2 = dict()

        result = 0

        for i in range(n):
            for j in range(n):
                part_sum = nums1[i] + nums2[j]
                sum_counts1[part_sum] = sum_counts1.get(part_sum, 0) + 1

        for i in range(n):
            for j in range(n):
                part_sum = nums3[i] + nums4[j]
                sum_counts2[part_sum] = sum_counts2.get(part_sum, 0) + 1

        for part_sum in sum_counts1.keys():
            count1 = sum_counts1[part_sum]
            count2 = sum_counts2.get(-part_sum, 0)
            result += count1 * count2

        return result

s = Solution()
# print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
# print(s.fourSumCount([1], [-1], [0], [1]))
print(s.fourSumCount(
[-1,1,1,1,-1],
[0,-1,-1,0,1],
[-1,-1,1,-1,-1],
[0,1,0,-1,-1]
))