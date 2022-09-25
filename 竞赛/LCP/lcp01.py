from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum([1 for i, j in zip(guess, answer) if i == j])