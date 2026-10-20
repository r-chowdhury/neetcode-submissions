class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for letter in s:
            if letter in s_map:
                s_map[letter] += 1
            else:
                s_map[letter] = 1
        for letter in t:
            if letter not in s_map:
                return False
            s_map[letter] -= 1
        for k in s_map:
            v = s_map[k]
            if v != 0:
                return False
        return True
