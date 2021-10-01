# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in set(nums):
            while nums.count(num) != 1:
                nums.pop(nums.index(num))