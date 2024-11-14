# 给定单词组和整数N,找出其中频率最低的N个单词，对于频率相同的单词按照字母顺序保留排序靠前的单词，输出按照先后顺序依次输出单词名称和出现次数
# 例如
from collections import Counter

words = ['how', 'how', 'are', 'are', 'you']
n = 3
# ans = "how-2,are-2,you-1"


class Solution:
    def lessNFrequent(self, words, n):
        word_count = Counter(words)
        # 按频率升序排列，频率相同的按字母顺序排列
        sorted_words = sorted(word_count.items(), key=lambda x: (x[1], x[0]))
        # 获取频率最低的N个单词
        least_frequent_words = sorted_words[:n]
        # 格式化输出
        valid_words = [w[0] for w in sorted_words]
        valid_words = sorted(valid_words, key=lambda w:words.index(w))
        result = ",".join(f"{word}-{word_count[word]}" for word in valid_words)
        return result


if __name__ == '__main__':
    solution = Solution()
    words = ['how', 'how', 'are', 'are', 'you']
    n = 2
    res = solution.lessNFrequent(words, n)
    print(res)