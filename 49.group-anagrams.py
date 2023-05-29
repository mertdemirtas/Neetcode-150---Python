#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for element in strs:
            temp = [0] * 26
            for ch in element:
                temp[ord(ch) - 97] += 1
            dic[tuple(temp)].append(element)
        return dic.values()
# @lc code=end

