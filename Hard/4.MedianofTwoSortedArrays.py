#My solution O((m+n) log(m+n))

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined = nums1 + nums2
        combined = sorted(combined, key=int, reverse=False)
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 == 0:
            median = (combined[(m+n)//2 -1] + combined[(m+n)//2]) / 2
        else:
            median = combined[(m+n)//2]
        return median
    