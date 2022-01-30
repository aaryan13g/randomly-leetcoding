/* https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/ */

class WordDictionary:

    def __init__(self):
        self.worddict = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.worddict[len(word)].append(word)

    def search(self, word: str) -> bool:
        if word in self.worddict[len(word)]:
            return True
        for w in self.worddict[len(word)]:
            for i in range(len(w)):
                if i == len(w) - 1 and (word[i] == '.' or word[i] == w[i]):
                    return True
                if word[i] == '.':
                    continue
                if word[i] != w[i]:
                    break
        return False
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
