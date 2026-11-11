#My solution O(n) where n = number of digits

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x = str(x)
        num_list = list(x)
        if num_list[0] == "-":
            sign = "-"
            num_list.pop(0)
        else:
            sign = ""
        reversed = num_list[::-1]
        while reversed[0] == "0":
            reversed.pop(0)
        result = ""
        for number in reversed:
            result += number
        result = sign + result
        result = int(result)
        if result <= -2**31 or result >= 2**31:
            return 0
        return(result)

solution = Solution()
print(solution.reverse(-83891))