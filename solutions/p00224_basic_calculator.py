def parse(s: str):
    expr = [1]
    sign = 1
    digits = ""
    cursor = [expr]

    def push_digit(d: str):
        nonlocal digits
        digits += d

    def push_sign(s: str):
        nonlocal sign
        nonlocal cursor

        flush_digits()

        if s == "+":
            sign = 1
        else:
            sign = -1

    def push_open_par():
        nonlocal cursor
        nonlocal sign

        new_ar = [sign]
        sign = 1
        cursor[len(cursor)-1].append(new_ar)
        cursor.append(new_ar)

    def push_close_par():
        nonlocal cursor
        flush_digits()
        cursor.pop()

    def flush_digits():
        nonlocal digits
        nonlocal sign

        if len(digits) > 0:
            cursor[len(cursor)-1].append(sign * int(digits))
            digits = ""
            sign = 1

    for char in s:
        if char == "(":
            push_open_par()
        elif char == ")":
            push_close_par()
        elif char == "+" or char == "-":
            push_sign(char)
        elif char.isnumeric():
            push_digit(char)
    flush_digits()
    print(expr)
    return expr

class Solution:
    def calculate(self, s: str) -> int:
        sum = 0
        last_sign = 1
        signs = [1]
        digits = ""

        for char in s + "#":
            if char.isnumeric():
                digits += char
            else:
                if len(digits) > 0:
                    sum += last_sign * signs[-1] * int(digits)
                    digits = ""
                if char == "+":
                    last_sign = 1
                elif char == "-":
                    last_sign = -1
                elif char == "(":
                    signs.append(last_sign * signs[-1])
                    last_sign = 1
                elif char == ")":
                    signs.pop()

        return sum


ss = "1 - (10 + (20 + 30))+5+(6-3)"
s = Solution()
print(s.calculate(ss))