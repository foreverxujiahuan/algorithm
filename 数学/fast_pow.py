

"""
快速幂
x^n
5^100
时间复杂度:O(n)
快速幂的时间复杂度O(log(n))
25^50
625^25
"""

if __name__ == '__main__':
    n = 5
    for _ in range(100):
        n = n * 5
    print(n)
