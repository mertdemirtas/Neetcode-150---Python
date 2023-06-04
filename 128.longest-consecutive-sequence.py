#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums) 
        res = 0

        for element in hashSet:
            if element - 1 not in hashSet:
                temp = element + 1
                currMax = 1
                while temp in hashSet:
                    currMax += 1
                    temp += 1
                res = max(res, currMax)
        return res
# @lc code=end

