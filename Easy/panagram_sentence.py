/* https://leetcode.com/problems/check-if-the-sentence-is-pangram/ */
  
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if set(sentence) == set('abcdefghijklmnopqrstuvwxyz'):
            return True
        else:
            return False
