

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        i = 0
        words1 = sentence1.split()
        words2 = sentence2.split()
        l1 = len(words1)
        l2 = len(words2)
        while i < l1 and i < l2 and words1[i] == words2[i]:
            i += 1
        words1 = words1[i:]
        words2 = words2[i:]
        j = 0
        while j < len(words1) and j < len(words2) and words1[-j-1] == words2[-j-1]:
            j += 1
        return i + j == min(l1, l2)


if __name__ == '__main__':
    sentence1 = "Eating right now"
    sentence2 = "Eating"
    solution = Solution()
    res = solution.areSentencesSimilar(sentence1, sentence2)
    print(res)
