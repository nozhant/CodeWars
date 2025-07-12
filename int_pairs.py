"""Pairs of integers from 0 to n: Write a function that accepts an integer argument n and generates an array containing the pairs of integers [a, b] that satisfy the condition
The pairs should be sorted by increasing values of a, then by increasing values of b.

link: https://www.codewars.com/kata/588e27b7d1140d31cb000060
"""

class Solution:

     def generate_pairs(self, n: int) -> list:

         result = []
         for a in range(n + 1):
             for b in range(a, n + 1):
                 result.append([a, b])
         return result

     def generate_pairs_one_line(self, n: int) -> list:

         return [[i, j] for i in range(n + 1) for j in range(i, n + 1)]





