# https://leetcode.com/submissions/detail/564009564/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li = []
        for i in range(len(nums)):
            if target - nums[i] in nums:
                pos = nums.index(target - nums[i])
                if pos != i:
                    li.append(i)
                    li.append(pos)
                    break
        return li