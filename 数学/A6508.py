class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7

        # 输入数据的长度
        L = len(pressedKeys)

        # dp[i] 表示从左边开始、**长度**为 i 的子字符串对应多少种文字信息
        # dp 长度比 pressedKeys 大 1, 用于处理长度为 0 的情况
        dp = [0] * (L + 1)

        # dp 初始化: 长度为 0, 有 1 种可能
        dp[0] = 1

        for i in range(L):
            ch = pressedKeys[i]  # 当前字符
            i = i + 1  # 下标 hack: dp 长度比 pressedKeys 大 1

            # 对于 '23456789', 至多连续按 3 下
            if i >= 1:
                dp[i] += dp[i - 1]
            if i >= 2:  # 最近 2 个字符相同
                if pressedKeys[i - 2] == pressedKeys[i - 1]:
                    dp[i] += dp[i - 2]
            if i >= 3:  # 最近 3 个字符相同
                if len(set(pressedKeys[i - 3:i])) == 1:
                    dp[i] += dp[i - 3]

            # 特别地, 对于'79', 至多连续按 4 下
            if ch in '79':
                if i >= 4:  # 最近 4 个字符相同
                    if len(set(pressedKeys[i - 4:i])) == 1:
                        dp[i] += dp[i - 4]

            dp[i] = dp[i] % MOD

        return dp[-1]


if __name__ == '__main__':
    pressedKeys = "222222222222222222222222222222222222"
    solution = Solution()
    res = solution.countTexts(pressedKeys)
    print(res)