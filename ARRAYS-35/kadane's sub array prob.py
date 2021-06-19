"""
Kadane's Algorithm 
Medium 
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)
"""


# simple sol.n

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        Sum = 0
        s1 = a[0]
        for i in range(size):
            Sum += a[i]
            if s1 < Sum:
                s1 = Sum
            if Sum < 0:
                Sum = 0

        return s1