#My solution O(n**3), i reused the same pointer tactic as in 3sum and problem 11, 
#but I took 2 initial numbers instead of 1 in 3 sum. 

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)-3):#-3 because when it reaches the last one there will be 3 more elements after it so last 4 tuple
            if i == 0 or nums[i] != nums[i-1]: #It removes duplicates of i index
                current1 = nums[i]
                for j in range(i+1,len(nums)-2): 
                    if j == i+1 or nums[j] != nums[j-1]: #It removes duplicates of j index
                        current2 = nums[j]
                        pointer1 = j+1
                        pointer2 = len(nums)-1
                        while pointer1 < pointer2:
                            curr_sum = current1 + current2 + nums[pointer1] + nums[pointer2]
                            if curr_sum == target:
                                if [current1, current2, nums[pointer1], nums[pointer2]] not in results: #Checks is we already have the 4sum
                                    results.append([current1, current2, nums[pointer1], nums[pointer2]])
                                pointer1 += 1
                                pointer2 -= 1
                            elif curr_sum < target: #Need a bigger number
                                pointer1 += 1
                            else:                   #Need a smaller number
                                pointer2 -= 1
        return results

solution = Solution()
print(solution.fourSum([-2,-1,-1,1,1,2,2], 0))