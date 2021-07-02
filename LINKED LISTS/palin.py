""" Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""using string"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        h1 = head
        s1 = ''
        while h1:
            s1 += str(h1.val)
            h1 = h1.next
        p1 = None
        p2 = head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        head = p1
        h2 = head
        s2 = ''
        while h2:
            s2 += str(h2.val)
            h2 = h2.next
        return s1 == s2


"""using lists"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0 , len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True


"""using six pointers"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True