#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        editedStr = ""
        reversedStr = ""
        for element in s:
            if(element.isalnum()):
               ch = element.lower()
               editedStr += ch
               reversedStr = ch + reversedStr
        return editedStr == reversedStr

        

# @lc code=end

