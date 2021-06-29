#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''

"""using single pointer and best sol."""

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here\
        # if head == None or head.next == None:
        #     return False
        # p1 = head
        # p2 = head
        # while (p1.next != None and p2.next.next != None):
        #     if p1.next == None or p2.next == None:
        #         return False
        #     if p1 == p2:
        #         return True
        #     print(p1.data,p2.data)
        #     p1 = p1.next
        #     p2 = p2.next.next
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