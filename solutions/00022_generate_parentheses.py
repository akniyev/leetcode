from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = dict()

        def get_variants_par(n: int) -> List[str]:
            if n == 1:
                memo[n] = ["()"]
                return ["()"]

            result = set()

            n_min_one_variants = get_variants_par(n-1)
            for variant in n_min_one_variants:
                result.add(f"({variant})")

            for i in range(1, n):
                vars1 = get_variants_par(i)
                vars2 = get_variants_par(n - i)
                for var1 in vars1:
                    for var2 in vars2:
                        result.add(var1 + var2)

            return result

        return list(get_variants_par(n))


s = Solution()
print(s.generateParenthesis(4))