#My solution O(n**2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)
            if len(odd) > len(longest_palindrome):
                longest_palindrome = odd
            if len(even) > len(longest_palindrome):
                longest_palindrome = even
        return longest_palindrome

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]