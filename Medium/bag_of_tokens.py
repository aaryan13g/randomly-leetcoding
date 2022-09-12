# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maxx = 0
        tokens.sort()
        l, r = 0, len(tokens) - 1
        while l <= r:
            if score <= 0 and power < tokens[l]:
                break
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                maxx = max(score, maxx)
                l += 1
            else:
                power += tokens[r]
                score -= 1
                r -= 1
        return maxx
