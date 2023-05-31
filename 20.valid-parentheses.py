#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {"}": "{", "]": "[", ")": "("}
        for ch in s:
            if ch in hashMap and len(stack) > 0:
                if hashMap[ch] != stack.pop():
                    return False
            else: 
                stack.append(ch)
        return len(stack) == 0
# @lc code=end

