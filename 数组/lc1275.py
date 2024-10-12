from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        target_list = [{(0, 0), (0, 1), (0, 2)},
                       {(1, 0), (1, 1), (1, 2)},
                       {(2, 0), (2, 1), (2, 2)},

                       {(0, 0), (1, 0), (2, 0)},
                       {(0, 1), (1, 1), (2, 1)},
                       {(0, 2), (1, 2), (2, 2)},

                       {(0, 0), (1, 1), (2, 2)},
                       {(0, 2), (1, 1), (2, 0)},
                   ]
        A = set()
        B = set()
        flag = 'A'
        d = {"A": 'B',
             'B': "A"}
        for move in moves:
            if flag == 'A':
                A.add(tuple(move))
            else:
                B.add(tuple(move))
            flag = d.get(flag)
            for target in target_list:
                if target.issubset(A):
                    return 'A'
                if target.issubset(B):
                    return "B"
        if len(moves) != 9:
            return "Pending"
        return "Draw"

if __name__ == '__main__':
    solution = Solution()
    moves = [[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]
    res = solution.tictactoe(moves)
    print(res)
    # a = tuple([1,2])
    # print(a)