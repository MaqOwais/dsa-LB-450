"""
Reverse a String 
Basic Accuracy: 56.22% Submissions: 35035 Points: 1
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
Example 2:

Input:
s = for
Output: rof
"""


def reverseWord(s):
    s1 = ''
    for i in range(len(s) - 1, -1, -1):
        s1 += s[i]
    return s1

def revArray(arr):
    s1 = []
    for i in range(len(arr) - 1, -1, -1):
        s1.append(arr[i])
    return s1


if __name__ == '__main__':
    # s = 'giver not taker'
    s1 = [1,2,3,4,5,6]
    # ans = reverseWord(s)
    ans = revArray(s1)
    print(ans)