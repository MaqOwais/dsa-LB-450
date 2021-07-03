#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''

"""using single pointer and best and illegal sol."""

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        while head.next != None:
            head.data = None
            head = head.next
            if head.data is None:
                return True
        return False

"""using 2 pointer approach"""
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow = head
        fast = slow.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

"""using dict is the fastest soln with more memory which maybe due to using extra dict data structure"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        di = {}
        t = head
        while t:
            if t == None or t.next == None:
                return False
            if t in di:
                return True
            di[t] = 1
            t = t.next
        return False
