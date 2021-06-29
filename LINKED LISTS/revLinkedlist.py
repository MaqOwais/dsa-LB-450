"""
Reverse a linked list 
Easy Accuracy: 48.93% Submissions: 100k+ Points: 2
Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.
Example 2:

Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.

for exp --> https://www.youtube.com/watch?v=bjtMCwy_LMA&ab_channel=ApnaCollege
problem link --> https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1#
"""

# Node Class
"""iterative approach"""
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head = prev
        return head

"""recursive approach"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        if head.next == None or head == None:
            return head
        newH = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newH
