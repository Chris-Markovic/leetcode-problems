#My solution O(n), I save the opening brackets into a list with currently open

class Solution:
    def isValid(self, s: str) -> bool:
        curr_open = []
        mapping = {")":"(","}":"{","]":"["}
        opening = ["(", "{", "["]
        for char in s:
            if char in opening:
                curr_open.append(char)
            elif len(curr_open) != 0:
                if mapping[char] == curr_open[-1]:
                    curr_open.pop(-1)
                else:
                    return False
            else:
                return False
            
        if len(curr_open) == 0:
            return True
        else:
            return False
        
solution = Solution()
print(solution.isValid("[([]])"))