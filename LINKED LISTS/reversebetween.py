"""
92. Reverse Linked List II
Medium

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

link -->https://leetcode.com/problems/reverse-linked-list-ii/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dum = ListNode(0)
        dum.next = head
        prev = dum
        cur = head
        cntr = 1
        while cur:
            if cntr >= left and cntr <= right-1:
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            else:
                prev = cur
                cur = cur.next
            cntr +=1

        return head
