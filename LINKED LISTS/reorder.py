"""Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

link --> https://leetcode.com/problems/reorder-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        li = []
        while head:
            li.append(head)
            head = head.next
        i = 0
        j = len(li) - 1
        while i < j:
            li[i].next = li[j]
            li[i] = li[i].next
            li[i].next = li[i + 1]
            
            i += 1
            j -= 1
        li[i].next = None

"""2nd approach"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,l):
        prev = None
        cur = l
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    def reorderList(self, head: ListNode) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        cur = mid.next
        mid.next = None
        right = self.reverse(cur)
        left = head

        while right:
            temp = left.next
            left.next = right
            left = temp
            temp = right.next
            right.next = left
            right = temp

        if left and right:
            right.next = left