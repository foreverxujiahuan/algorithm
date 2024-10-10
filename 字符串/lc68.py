from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur_words = []
        cur_length = 0
        for word in words:
            if not cur_words:
                cur_words.append(word)
                cur_length += len(word)
            else:
                word_cnt = len(cur_words)
                least_space_cnt = word_cnt - 1
                if least_space_cnt + cur_length + 1 + len(word) <= maxWidth:
                    cur_words.append(word)
                    cur_length += len(word)
                # 加不进去了
                else:
                    left_space_cnt = maxWidth - cur_length
                    while left_space_cnt:
                        for i in range(len(cur_words)):
                            if left_space_cnt:
                                cur_words[i] += " "
                                left_space_cnt -= 1
                            else:
                                break
                    cur_str = "".join(cur_words)
                    ans.append(cur_str)
                    cur_words = [word]
                    cur_length = len(word)
        if cur_words:
            left_space_cnt = maxWidth - cur_length
            while left_space_cnt:
                for i in range(len(cur_words)):
                    if left_space_cnt:
                        cur_words[i] += " "
                        left_space_cnt -= 1
                    else:
                        break
            cur_str = "".join(cur_words)
            ans.append(cur_str)
        return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    res = solution.fullJustify(words, maxWidth)
    print(res)
    for t in res:
        print(t)


