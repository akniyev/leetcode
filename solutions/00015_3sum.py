from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        frequences = dict()
        result = set()
        for num in nums:
            frequences[num] = frequences.get(num, 0) + 1

        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                s = -(nums[i] + nums[j])
                frequences[nums[i]] -= 1
                frequences[nums[j]] -= 1
                if frequences.get(s, 0) > 0:
                    result.add(tuple(sorted([nums[i], nums[j], s])))
                frequences[nums[i]] += 1
                frequences[nums[j]] += 1

        return list(result)

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
