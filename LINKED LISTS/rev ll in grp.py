"""
Reverse a Linked List in groups of given size. 
Medium Accuracy: 45.83% Submissions: 88116 Points: 4
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.
Example 2:

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.
"""


"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
# Reverse the first sub-list of size k. 
# While reversing keep track of the next node and previous node.
# Keep two pointers, pointer to the next node be next and 
# pointer to the previous node be prev.
# Recursively call for rest of the list 
# and link the two sub-lists. /* (head->next=reverse(next, k)) */
# prev becomes the new head of the list.

class Solution:
    def reverse(self,head, k):
        prev = None
        cur = head
        cntr = k
        while cntr > 0 and cur is not None:
            cntr -= 1
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # head = prev

        if nxt != None:
            head.next = self.reverse(nxt, k)
        return prev
            
        