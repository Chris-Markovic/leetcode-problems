#My solution O(m*n), I select the current letter which is in the first string in the list at index i, 
#then I compare all other letters at index i. If they all match. it does nothing. 
#If they dont match, it returns the current longest prefix.
#To not run into "out of range" issues in the for loop, i set it to the length of the shortest string, 
#since the prefix cant be longer than the shortest string anyway and it wont go out of bounds.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_substring = ""
        shortest_string = min(strs, key=len)
        for i in range(len(shortest_string)):
            current = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == current:
                    pass
                else:
                    return longest_substring
            longest_substring += current
        return longest_substring
            

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))

        