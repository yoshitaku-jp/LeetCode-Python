#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix

        for i in zip(*strs):
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                return prefix

        return prefix


# @lc code=end
