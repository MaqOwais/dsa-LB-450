"""
 Remove Linked List Elements
Easy

2915

129

Add to List

Share
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


link --> https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""iterative approach"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        prev = None
        while cur:
            if cur.val == val:
                if cur == head:
                    cur = head = head.next
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:    
                prev = cur
                cur = cur.next
        return head


"""recursive soln."""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None: 
            return None
        head.next = self.removeElements(head.next, val);
        if head.val == val:
            return head.next
        return head