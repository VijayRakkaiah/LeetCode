class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        list1 = s1.split()
        lastWord: str = list1[-1]
        length = len(lastWord)
        #sol = 'The last word is "%s" with length %i'%(lastWord, length)
        return length

result = Solution()
print(result.lengthOfLastWord('Hello World'))