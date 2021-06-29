"""
Count pairs with given sum 
Easy Accuracy: 41.59% Submissions: 48428 Points: 2
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, X = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.
"""


class Solution:
    def getPairsCount(self, arr, n, k):
    	m = [0] * 1000000
    	for i in range(0, n):
    		m[arr[i]] += 1
    	twice_cnt = 0
    	for i in range(0, n):
    		twice_cnt += m[k - arr[i]]
    		if (k - arr[i] == arr[i]):
    			twice_cnt -= 1
    	return int(twice_cnt / 2)
