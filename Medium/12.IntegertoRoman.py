#My solution O(n) - n = num of digits. I used a dict approach because the lookups are really fast and the amount of elements needed inside it wasnt that much
#I also considered an approach with separate lists for singles, tens, hundreds and thousands but the dict approach seemed easier
#If the number could be higher than 3999 as written by the constraints, this approach would be less effficient, but for this task it works well

class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = {"0":"","1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX", "10":"X", "20":"XX", "30":"XXX", "40":"XL",
                   "50":"L","60":"LX","70":"LXX","80":"LXXX", "90":"XC", "100":"C", "200":"CC", "300":"CCC", "400":"CD", "500":"D", "600":"DC", "700":"DCC", "800":"DCCC", "900":"CM", 
                   "1000":"M", "2000":"MM", "3000":"MMM"}
        roman = ""
        num = str(num)
        if num in numbers:
            return numbers[num]
        else:
            for i in range(len(num)):
                current_number = int(num[i])*(10**(len(num)-i-1))
                roman += numbers[str(current_number)]
            return roman
                
solution = Solution()
print(solution.intToRoman(3749))