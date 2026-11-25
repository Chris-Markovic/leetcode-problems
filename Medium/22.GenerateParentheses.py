#My solution O(4**n / sqrt(n)), I used a similar approach as problem 17 by bulding combinations
#and buidling them only if they are valid

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]

        combinations = [""]
        new_combinations = []
        for i in range(2*n):
            for combination in combinations:
                if combination.count("(") < n:
                    new_combinations.append(combination + "(")
                
                if combination.count("(") > combination.count(")"):
                    new_combinations.append(combination + ")")
                
            combinations = new_combinations
            new_combinations = []
        return combinations

    