#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for element in nums:
            if element in res:
                return True
            res.add(element)
        return False
            
# @lc code=end

