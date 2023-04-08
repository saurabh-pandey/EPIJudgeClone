from typing import List

def convert(n: int) -> List[int]:
    if n == 0:
        return [0]
    sign = 1 if n > 0 else -1
    n = abs(n)
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    digits[0] *= sign
    return digits
