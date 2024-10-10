# extracting n-grams from a sentence (20 pts)
# Complete the function get_ngrams, which takes a list of strings and an integer n as input, and returns padded n-grams over the list of strings. The result should be a list of Python tuples.
#
# For example:
#
# >>> get_ngrams(["natural","language","processing"],1)
# [('START',), ('natural',), ('language',), ('processing',), ('STOP',)]
# >>> get_ngrams(["natural","language","processing"],2)
# ('START', 'natural'), ('natural', 'language'), ('language', 'processing'), ('processing', 'STOP')]
# >>> get_ngrams(["natural","language","processing"],3)
# [('START', 'START', 'natural'), ('START', 'natural', 'language'), ('natural', 'language', 'processing'), ('language', 'processing', 'STOP')]

from typing import List, Tuple


class Solution:
    def get_ngrams(self, words: List, n: int) -> List[Tuple]:
        words = ['START'] * max(1, (n-1)) + words + ['STOP']
        return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]


if __name__ == '__main__':
    words = ["natural", "language", "processing"]
    n = 1
    ans = Solution()
    a = ans.get_ngrams(words, n)
    print(a)