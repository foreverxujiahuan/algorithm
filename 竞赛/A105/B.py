from typing import List


from typing import Dict, List, Any
import queue


class MatchTerm:
    def __init__(
            self,
            text: str,
            start_index: int,
            end_index: int,
            tag: str
    ) -> None:
        self.text = text
        self.start_index = start_index
        self.end_index = end_index
        self.tag = tag


class ForwardMaximumMatcher:
    """基于前缀词典的正向最大匹配"""

    def __init__(self, word2tag_dict: Dict[str, Any]) -> None:
        self.word2tag_dict = word2tag_dict
        self.prefix_set = set()
        for word, tag in self.word2tag_dict.items():
            for i in range(1, len(word)+1):
                self.prefix_set.add(word[0:i])

    def match(self, term_list: List[str]) -> List[MatchTerm]:
        match_word_list = []
        i = 0
        while i < len(term_list):
            stack = queue.LifoQueue()
            j = i
            while j < len(term_list):
                word = self.list_to_string(term_list[i:j+1])
                j += 1
                if word in self.prefix_set:
                    if word in self.word2tag_dict.keys():
                        tag = self.word2tag_dict[word]
                        stack.put(MatchTerm(word, i, j, tag))
                else:
                    break
            if not stack.empty():
                top_tag_term = stack.get()
                match_word_list.append(top_tag_term)
                i = top_tag_term.end_index
            else:
                i += 1
        return match_word_list

    @staticmethod
    def list_to_string(lst: List[str]) -> str:
        return "".join(lst)



class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ffm = ForwardMaximumMatcher(word2tag_dict={c: 0 for c in dictionary})
        ffm_res = ffm.match(list(s))
        length = 0
        for c in ffm_res:
            length += len(c.text)
        return len(s) - length

if __name__ == '__main__':
    s = "sayhelloworld"
    dictionary = ["hello","world"]
    solution = Solution()
    res = solution.minExtraChar(s, dictionary)
    print(res)

