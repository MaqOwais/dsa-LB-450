"""
Remove duplicate element from sorted Linked List 
Easy Accuracy: 46.37% Submissions: 93842 Points: 2
Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.

Example 1:

Input:
LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list 
2 ->2 -> 4-> 5, only 2 occurs more 
than 1 time.
Example 2:

Input:
LinkedList: 2->2->2->2->2
Output: 2
Explanation: In the given linked list 
2 ->2 ->2 ->2 ->2, 2 is the only element
and is repeated 5 times.

link --> https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1#
"""

#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    cur = head
    nxt = head.next
    while nxt:
        if cur.data == nxt.data:
            cur.next = nxt.next
        else:
            cur = nxt
        nxt = cur.next
    return head