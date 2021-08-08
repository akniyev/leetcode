from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        result = []

        def rec(i, partial_str):
            nonlocal digits
            nonlocal n
            nonlocal result

            if i >= n:
                if len(partial_str) > 0:
                    result.append(partial_str)
                return

            digit = digits[i]
            candidates = d[digit]
            for char in candidates:
                rec(i + 1, partial_str + char)
        rec(0, "")
        return result

s = Solution()
print(s.letterCombinations("23"))