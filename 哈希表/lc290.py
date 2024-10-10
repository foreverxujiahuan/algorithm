

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        ch2word = dict()
        word2ch = dict()
        if len(pattern) != len(words):
            return False
        for word, ch in zip(words, pattern):
            if ch not in ch2word and word not in word2ch:
                ch2word[ch] = word
                word2ch[word] = ch
            else:
                if ch not in ch2word or word not in word2ch or ch2word[ch] != word or word2ch[word] != ch:
                    return False
        return True


if __name__ == '__main__':
    pattern = "abc"
    s = "dog cat dog"
    solution = Solution()
    res = solution.wordPattern(pattern, s)
    print(res)