"""Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        s1 = ""
        s2 = ""
        while n1:
            s1 += str(n1.val)
            n1 = n1.next
        while n2:
            s2 += str(n2.val)
            n2 = n2.next
        summ = int(s1[::-1]) + int(s2[::-1])
        suma = str(summ)
        li = ListNode(0)
        pr = li
        for i in range(len(suma) - 1,-1,-1):
            pr.next = ListNode(int(suma[i]))
            pr = pr.next
        return li.next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # Set dummy node at head
    dummy = cur = ListNode(0)
    
    su = 0
    
    while l1 or l2 or su: # if either is not None
        
        # Cal. sum
        su += (l1.val if l1 else 0) + (l2.val if l2 else 0)
    
        # Cal. cur
        cur.next = ListNode(su % 10)
        cur = cur.next
    
        # Cal. carry
        su //= 10
    
        # Move forward
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
    
    # return
    return dummy.next