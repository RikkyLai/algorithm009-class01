#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist = 1
        wordList = set(wordList)
        front = [beginWord]
        if endWord not in wordList:
            return 0
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c!=word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word == endWord:
                                return dist
                            elif new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
        return 0

        
# @lc code=end

