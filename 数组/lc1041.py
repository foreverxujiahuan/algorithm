class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur = [0, 0]
        toward = 'N'
        instructions = instructions * 20
        for instruction in instructions:
            if instruction == 'G':
                if toward == 'N':
                    cur[1] += 1
                if toward == 'S':
                    cur[1] -= 1
                if toward == 'E':
                    cur[0] += 1
                if toward == 'W':
                    cur[0] -= 1
            if instruction in "LR":
                if toward == 'N' and instruction == 'L':
                    toward = 'W'
                elif toward == 'N' and instruction == 'R':
                    toward = 'E'
                elif toward == 'S' and instruction == 'L':
                    toward = 'E'
                elif toward == 'S' and instruction == 'R':
                    toward = 'W'
                elif toward == 'E' and instruction == 'L':
                    toward = 'N'
                elif toward == 'E' and instruction == 'R':
                    toward = 'S'
                elif toward == 'W' and instruction == 'L':
                    toward = 'S'
                elif toward == 'W' and instruction == 'R':
                    toward = 'N'
        if cur != [0, 0] and toward == 'N':
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    res = solution.isRobotBounded(instructions="GGLLGG")
    print(res)