"""
Reorder List
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
class Solution:
    """
        Reverse a given linked list starting at head
        
        Runtime: O(|list|)
        Space: O(1)
    """
    def reverseList(self, head: ListNode) -> None:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
            
    
    """
        Approach:  1  2  3  4  5
             left part   |  right part
                        mid
        Find mid, reverse right part, iterate through left part, and finally, interleave right and left.
        
        Runtime: O(|list|)
        Space: O(1)
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Find midpoint node using slow and fast pointer approach
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow
        
        # Reverse right part
        cur = mid.next
        mid.next = None
        right = self.reverseList(cur)
        
        # Interleave right and left parts
        cur_left = head
        cur_right = right

        while cur_right:
            temp = cur_left.next
            cur_left.next = cur_right
            cur_left = temp
            temp = cur_right.next
            cur_right.next = cur_left
            cur_right = temp
            
        if cur_left and cur_right:
            cur_right.next = cur_left
            
        return head
