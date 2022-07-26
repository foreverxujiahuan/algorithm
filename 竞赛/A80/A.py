class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if password == password.lower():
            return False
        if password == password.upper():
            return False
        if not set(password).intersection("0123456789"):
            return False
        if not set(password).intersection("!@#$%^&*()-+"):
            return False
        length = len(password)
        if length < 8:
            return False
        for i in range(length - 1):
            if password[i] == password[i+1]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    password = "ziyS5FrPQhoQ5oEWRpHW2MjI7sGfcMJdcsjQnIyRbdCilvFaQN07jQtAkOklbjFrU5KcHzw4EvJ41Yz2Ykyd"
    res = solution.strongPasswordCheckerII(password)
    print(res)

