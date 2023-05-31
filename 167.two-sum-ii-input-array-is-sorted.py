#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            temp = numbers[l] + numbers[r]

            if temp > target:
                r -= 1
            if temp < target:
                l += 1
            if temp == target:
                return [l + 1, r + 1]
        return [0,0]
# @lc code=end

