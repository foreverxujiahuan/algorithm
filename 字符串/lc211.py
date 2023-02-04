class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        for target in self.words:
            flag = 0
            if len(target) != len(word):
                flag = 1
            for c1, c2 in zip(word, target):
                if c1 != '.' and c1 != c2:
                    flag = 1
            if flag == 0:
                return True
        return False
