#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in dic:
                return [dic[res], i]
            dic[nums[i]] = i
        return [0,0]
# @lc code=end

