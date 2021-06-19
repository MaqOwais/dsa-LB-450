"""
Sort an array of 0s, 1s and 2s 
Easy Accuracy: 51.36% Submissions: 85481 Points: 2
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.

link --> https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1#
"""

# method 1 using count and replacing

def sort012(arr,n):
    c1 = 0
    c2 = 0
    c3 = 0
    
    for i in arr:
        if i == 0:
            c1 += 1
        elif i == 1:
            c2 += 1
        elif i == 2:
            c3 += 1
    j = 0
    while c1>0:
        arr[j] = 0
        j += 1
        c1 -= 1
    while c2 > 0:
        arr[j] = 1
        j += 1
        c2 -= 1
    while c3 > 0:
        arr[j] = 2
        j += 1
        c3 -= 1
    return arr


# METHOD 2 --> USING 3 POINTERS

def sort012(arr,n):
    ptL = 0
    ptH = n - 1
    ptM = 0
    
    while ptM <= ptH:
        if arr[ptM] == 0:
            arr[ptL], arr[ptM] = arr[ptM], arr[ptL]
            ptM += 1
            ptL += 1
        elif arr[ptM] == 1:
            ptM += 1
        else:
            arr[ptH], arr[ptM] = arr[ptM], arr[ptH]
            ptH -= 1

    return arr
        