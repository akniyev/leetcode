from typing import *


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if bool(dividend < 0) != bool(divisor < 0):
            sign = -1
        max_value = 2147483647 if sign == 1 else 2147483648
        result = 0
        remaining_dividend = abs(dividend)
        positive_divisor = abs(divisor)
        while remaining_dividend >= positive_divisor:
            num_of_divisors = 1
            sum_of_divisors = positive_divisor
            while sum_of_divisors <= remaining_dividend - sum_of_divisors:
                num_of_divisors += num_of_divisors
                sum_of_divisors += sum_of_divisors

            result = min(max_value, result + num_of_divisors)
            remaining_dividend -= sum_of_divisors
        return result if sign == 1 else -result

s = Solution()
print(s.divide(-2147483648, -1))
