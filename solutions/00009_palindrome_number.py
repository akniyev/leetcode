from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        x0 = x
        while x0 > 0:
            digits.append(x0 % 10)
            x0 = x0 // 10

        for i in range((len(digits) - 1) // 2 + 1):
            if digits[i] != digits[-i-1]:
                return False
        return True

s = Solution()
print(s.isPalindrome(-1221))
