"""
Remove loop in Linked List 
Medium Accuracy: 47.96% Submissions: 100k+ Points: 4
Given a linked list of N nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X. If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present.  


Example 1:

Input:
N = 3
value[] = {1,3,4}
X = 2
Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|    
A loop is present. If you remove it 
successfully, the answer will be 1. 

Example 2:

Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output: 1
Explanation: The Linked list does not 
contains any loop. 

link --> https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1
"""


'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

"""using hash"""
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        hsh = {}
        pre = None
        while head is not None:
            if head in hsh:
                pre.next = None
                break
            hsh[head] = True
            pre = head
            head = head.next
        return pre

"""using set"""
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        s = set()
        cur = head
        while cur:
            if cur.next in s:
                cur.next = None
                break
            s.add(cur)
            cur = cur.next
