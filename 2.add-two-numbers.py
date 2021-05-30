#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = tmp = ListNode(0)
        carry = 0

        while l1 or l2:
            sum_value = carry
            if l1 != None:
                sum_value += l1.val
                l1 = l1.next
            if l2 != None:
                sum_value += l2.val
                l2 = l2.next
            carry = sum_value // 10
            tmp.next = ListNode(sum_value % 10)
            tmp = tmp.next

            if carry == 1:
                tmp.next = ListNode(carry)
        return result.next


# @lc code=end
