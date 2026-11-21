#My solution O(4**n * n) - brute force solution, but to find every combination it is necessary. 

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mappings = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl","6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = [""] #List for the loop to go over and add new letters to existing combination
    
        for digit in digits:
            new_combinations = [] #List to add new letters, cant do it in the list combinations because it would keep finding new combos
            for combination in combinations:
                for letter in mappings[digit]:
                    new_combinations.append(combination+letter)
            combinations = new_combinations
        return combinations

solution = Solution()
print(solution.letterCombinations("23"))