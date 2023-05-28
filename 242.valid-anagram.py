#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_1 = {}
        dic_2 = {}

        for element in s:
            dic_1[element] = 1 + dic_1.get(element, 0)
        for element in t:
            dic_2[element] = 1 + dic_2.get(element, 0)

        return dic_1 == dic_2
# @lc code=end

