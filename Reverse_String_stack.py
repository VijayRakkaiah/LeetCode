class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in s:
            stack.append(i)
        i = 0
        while len(stack)>0:
            a = stack.pop()
            s[i] = a
            i+=1



"""
344. Reverse String
PROBLEM:
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""