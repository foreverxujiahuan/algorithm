class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False