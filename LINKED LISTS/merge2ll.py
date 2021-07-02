"""
 Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        headNode = ListNode(0)
        root = headNode
        
        while l2 and l1:
            v1 = l1.val
            v2 = l2.val
            if v1 <= v2:
                headNode.next = l1
                l1 = l1.next
            else:
                headNode.next = l2
                l2 = l2.next
            headNode = headNode.next
        if l2:
            headNode.next = l2
        elif l1:
            headNode.next = l1
            
        return root.next

"""using recursion"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        v1 = l1.val
        v2 = l2.val
        
        if v1 <= v2:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2