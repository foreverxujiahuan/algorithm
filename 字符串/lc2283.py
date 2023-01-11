class Solution:
    def digitCount(self, num: str) -> bool:
        for i, c in enumerate(num):
            if int(c) != num.count(str(i)):
                return False
        return True


if __name__ == '__main__':
    pass