/* https://leetcode.com/problems/unique-morse-code-words/ */

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            temp = ""
            for ch in word:
                temp += morse_list[ord(ch) - 97]
            transformations.add(temp)
        return len(transformations)
