#My solution O(n)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        biggest = 0
        counter1 = 0
        counter2 = len(height)-1
        while counter1 != counter2:
            num1 = height[counter1]
            num2 = height[counter2]
            size = min(num1, num2) * (counter2 - counter1)
            if size > biggest:
                biggest = size
            if num1 < num2:
                counter1 += 1
                
            else:
                counter2 -= 1

        return biggest

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))