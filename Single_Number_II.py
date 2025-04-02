class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                if d[i]==1:
                    d[i]+=1
                else:
                    del d[i]
        single_num = list(d.keys())
        return single_num[0]

'''
137. Single Number II

PROBLEM:

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

'''