#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current = 0
        for i in logs:
            if "../" in i and current != 0:
                current -= 1
            elif "./" in i:
                continue
            else:
                current += 1
        return current


# @lc code=end
