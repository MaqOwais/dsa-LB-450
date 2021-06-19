"""Move all negative numbers to beginning and positive to end with constant extra space
Difficulty Level : Easy
Last Updated : 09 Jun, 2021
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
"""

def rearr(arr, n):
    j = 0
    for i in range(n):
        if (arr[i] > 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j += 1

    return A


if __name__ == '__main__':
    A = [2,55,-99,88,22,-33,12,90,-9,-7,-9]
    n = len(A)
    ans = rearr(A,n)
    print(ans)
