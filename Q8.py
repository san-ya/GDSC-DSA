# https://leetcode.com/problems/monotonic-array/submissions/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp1 = sorted(nums)
        temp2 = sorted(nums, reverse=True)
        
        return temp1 == nums or temp2 == nums