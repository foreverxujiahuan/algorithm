import matplotlib.pyplot as plt

plt.pie()

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum([i for i in range(1, n+1) if i % 3 == 0 or i % 3 == 0 or i % 7 == 0])