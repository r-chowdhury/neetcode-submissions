class PrefixTree:

    def __init__(self):
        self.res = []
        

    def insert(self, word: str) -> None:
        self.res.append(word)

    def search(self, word: str) -> bool:
        for w in self.res:
            if word == w:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        prefix_length = len(prefix)
        for w in self.res:
            if w[:prefix_length] == prefix:
                return True
        return False

        
        
        