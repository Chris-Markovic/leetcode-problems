"""
My solution O(m*n)

With * - table approach: create a 2D table with all False, 
then checks: does dp[i][j] = do the first i characters of s match the first j characters of p?
I used the help of AI to come up with the approach and coded it.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        #No special characters
        if "." not in p and "*" not in p:
            if s == p:
                return True
            else:
                return False

        #No * - easier case, either the letters match or the pattern has to have .
        elif "*" not in p:
            if len(s) != len(p):
                return False
            for i in range(len(s)):
                if s[i] == p[i] or p[i] == ".":
                    pass
                else:
                    return False
            return True
        
        #With *, explanation in the beginning
        else:
            dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
            dp[0][0] = True

            for j in range(2, len(p) + 1):
                if p[j-1] == "*":
                    dp[0][j] = dp[0][j-2]

            for i in range(1, len(s) + 1):
                for j in range(1, len(p) + 1):
                    if p[j-1] == "*":
                        zero = dp[i][j-2]
                        more = (s[i-1] == p[j-2] or p[j-2] == ".") and dp[i-1][j]
                        dp[i][j] = zero or more
                    else:
                        dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == ".") and dp[i-1][j-1]

            return dp[len(s)][len(p)]