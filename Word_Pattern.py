class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        print(words)
        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}
        for i in range(0, len(pattern)):
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = words[i]
            elif pattern[i] in pattern_to_word:
                value = pattern_to_word[pattern[i]]
                if value == words[i]:
                    continue
                else:
                    return False
            if words[i] not in word_to_pattern:
                word_to_pattern[words[i]] = pattern[i]
            elif words[i] in word_to_pattern:
                value = word_to_pattern[words[i]]
                if value == words[i]:
                    continue
                else:
                    return False
        return True