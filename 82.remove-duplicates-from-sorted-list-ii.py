#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next: # どちらかがnullになるまでおこなう
            if head.val == head.next.val: # 現在の値と次の値が同じ場合
                while head and head.next and head.val == head.next.val: # どれかがnullになるまでかつ、値が同じならループする
                    head = head.next # 次の値に移動
                head = head.next # 次の値に移動
                pre.next = head # 現在の値を前の値に挿入
            else:
                pre = pre.next
                head = head.next
        return dummy.next    

# @lc code=end

