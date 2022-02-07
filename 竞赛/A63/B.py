class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        length = len(colors)
        for i in range(1, length - 1):
            pre_ch = colors[i-1]
            cur_ch = colors[i]
            next_ch = colors[i+1]
            if cur_ch == pre_ch and cur_ch == next_ch:
                if cur_ch == 'A':
                    alice += 1
                else:
                    bob += 1
        if alice > bob:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    colors = "ABBBBBBBAAA"
    res = s.winnerOfGame(colors)
    print(res)
