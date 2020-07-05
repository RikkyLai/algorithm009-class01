#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.lookup
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        trie['#'] = '#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.lookup
        for w in word:
            if w not in trie:
                return False
            trie = trie[w]
        if '#' in trie:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.lookup
        for w in prefix:
            if w not in trie:
                return False
            trie = trie[w]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

