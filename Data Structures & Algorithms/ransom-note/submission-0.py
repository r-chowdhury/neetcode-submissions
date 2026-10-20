class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for s in magazine:
            if s in magazine_count:
                magazine_count[s] += 1
            else:
                magazine_count[s] = 1
        for s in ransomNote:
            if s not in magazine_count:
                return False
            
            if magazine_count[s] == 0:
                return False
            
            magazine_count[s] -= 1
        return True

        