"""Upside down numbers: Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

link: https://www.codewars.com/kata/59f7597716049833200001eb/python
"""

class Solution:

    def is_upside_down(self, n: int) -> bool:
        valid_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = str(n)
        try:
            flipped = ''.join(valid_pairs[c] for c in reversed(s))
            print(flipped)
        except KeyError:
            return False
        return s == flipped

    def solve(self, low: int, high: int) -> int:
        return sum(self.is_upside_down(n) for n in range(low, high))

