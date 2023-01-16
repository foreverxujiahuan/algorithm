from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        flag = 0
        name = ''
        d = {k: v for k, v in knowledge}
        for c in s:
            if c == '(':
                flag = 1
            elif c == ')' and flag:
                s = s.replace('(' + name + ')', d.get(name, "?"))
                name = ''
                flag = 0
            elif flag == 1:
                name += c
        return s


if __name__ == '__main__':
    s = "hi(name)"
    knowledge = [["a","b"]]
    solution = Solution()
    res = solution.evaluate(s, knowledge)
    print(res)

