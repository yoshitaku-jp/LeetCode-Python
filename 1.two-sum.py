#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            for j in range(len(nums) - 1, i, -1):
                if target == (val + nums[j]):
                    return [i, j]


# @lc code=end
