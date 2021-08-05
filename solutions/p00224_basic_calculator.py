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
        parsed = parse(s)

        def sum(items):
            if not isinstance(items, list):
                return items
            result = 0
            sig = items[0]
            for item in items[1:]:
                result += sig * sum(item)
            return result

        return sum(parsed)


ss = ""
s = Solution()
print(s.calculate(ss))