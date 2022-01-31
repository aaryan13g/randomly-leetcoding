/* https://leetcode.com/problems/reverse-prefix-of-word/ */

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = word.find(ch)
        if ind == len(word) - 1:
            return word[::-1]
        if ind != -1:
            return word[:ind + 1][::-1] + word[ind + 1:]
        return word
