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