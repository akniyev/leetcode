from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()

        nums_len = len(nums)
        nums.sort()

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                k = j + 1
                l = nums_len - 1
                while k < l:
                    temp_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if temp_sum == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                    elif temp_sum < target:
                        k += 1
                    else:
                        l -= 1

        return list(map(lambda tuple: list(tuple), result))

s = Solution()
print(s.fourSum([-3,-2,-1,0,0,1,2,3], 0))