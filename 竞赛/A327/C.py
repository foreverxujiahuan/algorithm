from collections import Counter
from string import ascii_lowercase


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        s1 = set(word1)
        s2 = set(word2)
        for c1 in s1:
            for c2 in s2:
                word_list1 = list(word1)
                word_list2 = list(word2)
                index1 = word_list1.index(c1)
                index2 = word_list2.index(c2)
                word_list1[index1] = c2
                word_list2[index2] = c1
                if len(set(word_list1)) == len(set(word_list2)):
                    return True
        return False



if __name__ == '__main__':
    word1 = "abcde"
    word2 = "fghij"
    solution = Solution()
    res = solution.isItPossible(word1, word2)
    print(res)