"""
The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
Find the largest index l greater than k such that a[k] < a[l].
Swap the value of a[k] with that of a[l].
Reverse the sequence from a[k + 1] up to and including the final element a[n].
from https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

"""

"""
31. Next Permutation
Medium

5949

1993

Add to List

Share
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind1 = -1
        ind2 = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                ind1 = i
        if ind1 == -1:
            nums.reverse()
            return
        for j in range(ind1 + 1, len(nums)):
            if nums[j] > nums[ind1]:
                ind2 = j

        nums[ind1],nums[ind2] = nums[ind2],nums[ind1]

        nums[ind1+1:] = nums[ind1+1:][::-1]

# other solns.

# class Solution:
#     def permuteUnique(self, nums):
#         res = []
#         self.dfs(sorted(nums), [], res)
#         return res

#     def dfs(self, nums, curr, res):
#         if not nums:
#             res.append(curr)
# 			return
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             self.dfs(nums[:i]+nums[i+1:], curr+[nums[i]], res)

# Solution 2 (tweaking the Permutations I solution):

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         self.helper(nums, [], res)
#         return list(res)
    
    
#     def helper(self, nums, curr, res):
#         if not nums:
#             res.add(tuple(curr))
#             return
#         for i in range(len(nums)):
#             self.helper(nums[:i]+nums[i+1:], curr + [nums[i]], res)
