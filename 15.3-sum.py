#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for l in range(len(nums) - 2):
            if nums[l] > 0:
                break
            r = len(nums) - 1
            mid = l + 1
            while mid < r:
                temp = nums[l] + nums[mid] + nums[r]
                if temp > 0:
                    r -= 1
                    continue
                if temp == 0:
                    res.add(tuple([nums[l], nums[mid], nums[r]]))
                mid += 1
        return res

# @lc code=end

