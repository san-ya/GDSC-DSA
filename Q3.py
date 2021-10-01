# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target) > 1:
            return [nums.index(target), nums.index(target) + nums.count(target) - 1]
        elif nums.count(target) == 1:
            return [nums.index(target), nums.index(target)]
        else:
            return [-1, -1]
        