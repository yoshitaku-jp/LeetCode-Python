#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        result_node = cur = ListNode(0)

        while True:
            if not l1:
                cur.next = l2
                break
            if not l2:
                cur.next = l1
                break

            if l1.val > l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            cur = cur.next
        return result_node.next


# @lc code=end
