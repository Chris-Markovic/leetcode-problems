#My solution O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
        s = s[::-1]
        number = 0
        for i in range(len(s)):
            current = numerals[s[i]]
            if i == 0:
                previous = 0
            else:
                previous = numerals[s[i-1]]
            if current < previous:
                number -= current
            else:
                number += current
        return number

solution = Solution()
print(solution.romanToInt("CDXIII"))