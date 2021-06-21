"""
Minimum number of jumps 
Medium Accuracy: 32.96% Submissions: 100k+ Points: 4
Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Example 1:

Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to last. 
Example 2:

Input :
N = 6
arr = {1, 4, 3, 2, 6, 7}
Output: 2 
Explanation: 
First we jump from the 1st to 2nd element 
and then jump to the last element.
"""

#User function Template for python3
# using ladder and stair approach (https://www.youtube.com/watch?v=vBdo7wtwlXs&ab_channel=IDeserveIDeserve)

def minJumps(arr, n):
    if len(arr) <= 1 : 
        return 0

    if arr[0] == 0:
        return -1
    lad = arr[0]
    stairs = arr[0]
    jump = 1

    for i in range(1, n):
        if i == n - 1:
            return jump
        nxt = i + arr[i]
        if nxt > lad:
            lad = nxt
        stairs -= 1
        if stairs == 0:
            jump += 1
            stairs = lad - i
            if stairs <= 0: 
                return -1

    return jump

if __name__ == "__main__":
    N = 11 
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    ans = minJumps(arr,N)
    print(ans)
