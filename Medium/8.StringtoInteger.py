#My solution O(n) where n is the length of the input string

class Solution:
    def myAtoi(self, s: str) -> int:
        string = list(s)
        i = 0

        #Step1
        while i < len(string) and string[i] == " ":
            i += 1

        #Step2
        sign = ""
        if i < len(string) and string[i] in ["-", "+"]:
            if string[i] == "-":
                sign = "-"
            i += 1

        #Step3
        final_number = ""
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while i < len(string) and string[i] in numbers:
            final_number += string[i]
            i += 1

        if len(final_number) == 0:
            return 0

        n = 0
        for number in final_number:
            n = n * 10 + int(number)
        if sign == "-":
            n = -n

        if n < -2**31:
            return -2**31
        elif n > 2**31 - 1:
            return 2**31 - 1
        else:
            return n
        
    
solution = Solution()
print(solution.myAtoi("1337c0d3"))