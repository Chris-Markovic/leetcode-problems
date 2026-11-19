#My solution O(n**2), I used a similar approach as in problem 11 with two pointers where a pointer is moved based on need
#meaning if we need a smaller number we move the pointer2 since the list is sorted so moving left always gives a lower number

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]: #It removes duplicates
                current = nums[i]
                pointer1 = i+1
                pointer2 = len(nums)-1
                needed = -1 * current
                while pointer1 < pointer2:
                    if nums[pointer1] + nums[pointer2] == needed:
                        results.append([current, nums[pointer1], nums[pointer2]])
                        pointer1 += 1
                        pointer2 -= 1
                        while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 - 1]: #Skips left values which are the same as we just used
                            pointer1 += 1
                        while pointer1 < pointer2 and nums[pointer2] == nums[pointer2 + 1]: #Skips right values which are the same as we just used
                            pointer2 -= 1
                    elif nums[pointer1] + nums[pointer2] < needed: #Need a bigger number
                        pointer1 += 1
                    else:       #Need a smaller number
                        pointer2 -= 1

        return results
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))