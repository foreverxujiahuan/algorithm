class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = str(num)
        num_list = list(num_str)
        num_list = sorted(num_list)
        num1 = int(int(num_list[0]) * 10) + int(num_list[3])
        num2 = int(int(num_list[1]) * 10) + int(num_list[2])
        return num1 + num2


if __name__ == '__main__':
    solution = Solution()
    num = 4009
    res = solution.minimumSum(num)
    print(res)