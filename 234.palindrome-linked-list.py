#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        head_list = []
        while True:
            if head.next is None :
                head_list.append(head.val)
                break
            elif head.next is not None :
                head_list.append(head.val)
                head = head.next

        j = len(head_list)-1
        for i in range(len(head_list)):
            if head_list[i] != head_list[j]:
                return False
            i += 1
            j -= 1
            if i > j == True:
                break

        return True




# @lc code=end

