class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x1 = x
            x2 = str(x)
            s = x2[::-1]
            x3 = int(s)
        if x3 == x1:
            return True
        else:
            return False
sol = Solution()
print(sol.isPalindrome(121))