class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_cnt = customers.count('Y')
        cur_y = 0
        cur_n = 0
        arr = []
        for ch in customers:
            arr.append(y_cnt - cur_y + cur_n)
            if ch == 'Y':
                cur_y += 1
            else:
                cur_n += 1
        arr.append(y_cnt - cur_y + cur_n)
        ans = arr.index(min(arr))
        if ans == len(customers) - 1 and customers[-1] == 'Y':
            return ans+1
        return arr.index(min(arr))


if __name__ == '__main__':
    customers = "N"
    solution = Solution()
    res = solution.bestClosingTime(customers)
    print(res)
