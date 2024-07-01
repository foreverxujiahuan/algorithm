MOD = 10 ** 9 + 7


def num_perms(n, requirements):
    max_inversions = n * (n - 1) // 2
    requirements_dict = {endi: cnti for endi, cnti in requirements}

    # Initialize DP table
    dp = [[[0] * (max_inversions + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    # Fill DP table
    for length in range(1, n + 1):
        for inv in range(max_inversions + 1):
            for used in range(length):
                for new_inv in range(min(used + 1, inv + 1)):
                    dp[length][inv][used + 1] = (dp[length][inv][used + 1] + dp[length - 1][inv - new_inv][used]) % MOD

    result = 0
    for inv in range(max_inversions + 1):
        valid = True
        for endi, cnti in requirements_dict.items():
            if dp[endi + 1][cnti][endi + 1] == 0:
                valid = False
                break
        if valid:
            result = (result + dp[n][inv][n]) % MOD

    return result


# 示例
print(num_perms(3, [[2, 2], [0, 0]]))  # 输出：2
print(num_perms(3, [[2, 2], [1, 1], [0, 0]]))  # 输出：1
print(num_perms(2, [[0, 0], [1, 0]]))  # 输出：1
