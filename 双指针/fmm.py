from typing import Dict, List

# from siren.nlu.utils.match_term import MatchTerm
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

    def __init__(self, word2tag_dict: Dict[str, str]) -> None:
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
                word = self.list_to_string(term_list[i: j+1])
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
            else :
                i += 1
        return match_word_list

    @staticmethod
    def list_to_string(chars: List[str]) -> str:
        return "".join(chars)


if __name__ == '__main__':
    word2dict = {
        "乒乓球": "球类",
        "乒乓球台": "大型体育器材",
        "乒乓球比赛": "比赛"
    }
    fmm = ForwardMaximumMatcher(word2tag_dict=word2dict)
    term_list = "我去参加乒乓球比赛了"
    term_list = list(term_list)
    match_terms = fmm.match(term_list)
    for match_term in match_terms:
        print(match_term.text, match_term.tag)
