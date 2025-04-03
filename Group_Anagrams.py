class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sorted_value = ''.join(sorted(i))
            if sorted_value not in d:
                d[sorted_value] = [i]
            else:
                d[sorted_value].append(i)
        output = list(d.values())
        return output

