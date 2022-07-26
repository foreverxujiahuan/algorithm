class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            length = len(s)
            temp = []
            if length % k == 0:
                l = length // k
            else:
                l = (length // k) + 1
            for i in range(l):
                t = s[i * k:(i + 1) * k]
                n = sum([int(j) for j in t])
                temp.append(str(n))
            s = "".join(temp)
        return s


if __name__ == '__main__':
    s = "11111222223"
    k =3
    solution = Solution()
    res = solution.digitSum(s, k)
    print(res)
