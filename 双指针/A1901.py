from typing import (
    List,
)

class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A: List[int]) -> List[int]:
        # write your code here
        return sorted([t*t for t in A])
