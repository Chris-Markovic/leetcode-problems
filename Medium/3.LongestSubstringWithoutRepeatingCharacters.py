#My solution O(n**3) - inefficient and slow solution, best solution = sliding window O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest_substring = s[0]
        for i in range(len(s)):
            counter = 1
            curr_substring = ""
            curr_letter = s[i]
            while curr_letter not in curr_substring:
                if i+counter >= len(s):
                    curr_substring += curr_letter
                    break
                else:
                    curr_substring += curr_letter
                    curr_letter = s[i + counter]
                    counter += 1
            if len(curr_substring) > len(longest_substring):
                longest_substring = curr_substring 
        return len(longest_substring)
