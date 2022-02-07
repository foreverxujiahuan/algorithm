arr1 = [5,7,7,8,7,7,6,7,7,8,8,6,8,9,10,11,12,12,11,10,8,9,8,10,12]
arr2 = [4,5,6,8,9,9,10,10,11,12,13,14,14,13,12,11,10,10,8,9,9,9]


class Solution:

    def get_parse(self, arr):
        output = []
        length = len(arr)
        kb2n = dict()
        index = 0
        for i in range(length - 1):
            k = arr[i+1] - arr[i]
            output.append(k)
            if k not in kb2n.keys():
                kb2n[k] = str(index)
                index += 1
        return [kb2n[t] for t in output]

    def get_max_length(self, arr1, arr2):
        parse1 = self.get_parse(arr1)
        parse2 = self.get_parse(arr2)
        res = self.lcs(parse1, parse2)
        return res

    def lcs(self, arr1, arr2):
        len_str1 = len(arr1)
        len_str2 = len(arr2)
        dp = [[0 for i in range(len_str2 + 1)] for j in range(len_str1 + 1)]
        for i in range(len_str1):
            for j in range(len_str2):
                if arr1[i] == arr2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                elif dp[i + 1][j] > dp[i][j + 1]:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    res = s.get_max_length(arr1, arr2)
    print(len(arr1), len(arr2))
    print(res)