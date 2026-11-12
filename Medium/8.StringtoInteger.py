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
        values = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        while i < len(string) and string[i] in values:
            final_number += string[i]
            i += 1

        if len(final_number) == 0:
            return 0

        n = 0
        for number in final_number:
            n = n * 10 + values[number]
        if sign == "-":
            n = -n

        if n < -2**31:
            return -2**31
        elif n > 2**31 - 1:
            return 2**31 - 1
        else:
            return n