class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_1 = 0
        pointer_2 = 0
        while (pointer_1 < len(s)) and (pointer_2 < len(t)):
            if s[pointer_1] == t[pointer_2]:
                pointer_1 += 1
                pointer_2 += 1
            else:
                pointer_2 += 1
        
        if pointer_1 == len(s):
            return True
        else:
            return False
            
"""
392. Is Subsequence
PROBLEM:

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""