"""Find the random seed: Given a list of random integers, return the integer used to initialize the random number generator (the "seed") (0 <= n < 10000)

The input list is comprised of the first 10 random integers between 0 and 100 (inclusive) produced after initializing the random number generator from the random module.

link: https://www.codewars.com/kata/5a106ce7ffe75f4c200000f7
"""

import random


class Solution:

    def find_seed(self, target_output: list):
        for seed in range(10000):
            random.seed(seed)
            generated = [random.randint(0, 100) for _ in range(10)]
            if generated == target_output:
                return seed
        return None