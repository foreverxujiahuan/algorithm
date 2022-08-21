from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        to_energy = max(0, sum(energy) - initialEnergy + 1)
        to_experience = 0
        for e in experience:
            if initialExperience < e:
                diff = e - initialExperience + 1
                to_experience += diff
                initialExperience += diff
            elif initialExperience == e:
                diff = 1
                to_experience += diff
                initialExperience += diff
            initialExperience += e
        ans = to_energy + to_experience
        return ans

if __name__ == '__main__':
    solution = Solution()
    initialEnergy = 5
    initialExperience = 3
    energy = [1, 4, 3, 2]
    experience = [2, 6, 3, 1]
    # initialEnergy = 2
    # initialExperience = 4
    # energy = [1]
    # experience = [3]
    # initialEnergy = 5
    # initialExperience = 3
    # energy = [1, 4]
    # experience = [2, 5]
    res = solution.minNumberOfHours(initialEnergy, initialExperience, energy, experience)
    print(res)
