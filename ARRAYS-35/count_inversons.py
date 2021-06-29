"""
Count Inversions 
Medium Accuracy: 39.43% Submissions: 69386 Points: 4
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.
Example 3:

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array 
are same, so there is no inversion count.

link for exp --> https://www.youtube.com/watch?v=jYww4YDOZEE&ab_channel=k%C5%8DdiNG
"""
class Solution:
    def inversionCount(self, arr, n):
        temp_arr = [0]*n
        return self._mergeSort(arr, temp_arr, 0, n-1)

    def _mergeSort(self,arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right)//2
            inv_count += self._mergeSort(arr, temp_arr, 
                                        left, mid)
            inv_count += self._mergeSort(arr, temp_arr, 
                                      mid + 1, right)
            inv_count += self.merge(arr, temp_arr, left, mid, right)
        return inv_count

    def merge(self,arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                k += 1
                j += 1
    
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
            
        return inv_count
