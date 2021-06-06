#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = list(str(x))
        for i in tmp:
            for j in reversed(tmp):
                if i != j:
                    return False
        return True


# @lc code=end
