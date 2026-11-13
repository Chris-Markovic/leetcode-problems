#My solution O(n) where n = the number of digits (and the sign if there is one)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_list = list(str(x))
        reversed = int_list[::-1]
        if int_list == reversed:
            return True
        else:
            return False