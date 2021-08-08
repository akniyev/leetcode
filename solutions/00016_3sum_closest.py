from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        min_sum = 0
        for i in range(n-2):
            if min_diff == 0:
                break

            target_sum = target - nums[i]
            i0 = i + 1
            j0 = n - 1
            while i0 < j0:
                s = nums[i0] + nums[j0]
                if abs(s - target_sum) < min_diff:
                    min_diff = abs(s - target_sum)
                    min_sum = nums[i] + nums[i0] + nums[j0]
                if s < target_sum:
                    i0 += 1
                else:
                    j0 -= 1

        return min_sum






















# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         r = None
#         for i in range(n-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, n-1):
#                 s = target - (nums[i] + nums[j])
#                 i0 = j + 1
#                 j0 = n - 1
#                 m = 0
#                 if s <= nums[i0]:
#                     m = i0
#                 elif s >= nums[j0]:
#                     m = j0
#                 else:
#                     while i0 < j0:
#                         if j0 - i0 == 1:
#                             if abs(nums[i0] - s) < abs(nums[j0] - s):
#                                 m = i0
#                             else:
#                                 m = j0
#                             break
#
#                         m = (i0 + j0) // 2
#                         if nums[m] == s:
#                             break
#                         elif nums[m] < s:
#                             i0 = m
#                         else:
#                             j0 = m
#                 sum = nums[i] + nums[j] + nums[m]
#                 if r is None:
#                     r = sum
#                 elif abs(r - target) > abs(sum - target):
#                     r = sum
#         return r

s = Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
