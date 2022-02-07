from typing import (
    List,
)

class Solution:
    """
    @param costPerCut: integer cost to make a cut
    @param salePrice: integer per unit length sales price
    @param lengths: an array of integer rod lengths
    @return: The function must return an integer that denotes the maximum possible profit.
    """
    def maxProfit(self, costPerCut: int, salePrice: int, lengths: List[int]) -> int:
        # write your code here
        return max((sum((length - length % cut_length) * salePrice for length in lengths) - sum([costPerCut * int((length - 0.1) / cut_length) for length in lengths])) for cut_length in range(1, max(lengths) + 1))

    def test(self, costPerCut: int, salePrice: int, lengths: List[int]) -> int:
        return max((sum((length - length % cut_length) * salePrice for length in lengths) - sum([costPerCut * int((length - 0.1) / cut_length) for length in lengths])) for cut_length in range(1, max(lengths) + 1))


if __name__ == '__main__':
    solution = Solution()
    costPerCut = 5
    salePrice = 4
    lengths = [15,13,24,5,9]
    res = solution.maxProfit(costPerCut, salePrice, lengths)
    print(res)

