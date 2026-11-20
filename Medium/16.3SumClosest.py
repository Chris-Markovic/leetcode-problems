#My solution O(n**2) - same as the problem 15 since its the same approach
#I reused the logic from problem 15 to search sums of three nums,
#then i compared the distance of the current pair sum and the closest, changing it if its lower

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = 10000000 # Sets the closest high so that the first match is always closer
        for i in range(len(nums)-2):
            current = nums[i]
            pointer1 = i+1
            pointer2 = len(nums)-1
            while pointer1 < pointer2: #Same pointer technique as in problem 15
                current_sum = current + nums[pointer1] + nums[pointer2]
                if current_sum == target: #If it matches the target exactly, we can return the target since a closer match doesnt exist
                    return target
                elif current_sum < target:
                    pointer1 += 1
                else:
                    pointer2 -= 1
                if abs(target - current_sum) < abs(target - closest): #Checks if the distance of the current sum is smaller than the distance of smallest found
                    closest = current_sum
                    
            
        return closest

solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1)) #2