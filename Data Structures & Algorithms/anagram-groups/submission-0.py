class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = {}
      for s in strs:
        count = [0] * 26
        for c in s:
          count[ord(c) - ord('a')] += 1
        temp = tuple(count)
        if temp in res:
          res[temp].append(s)
        else:
          res[temp] = [s]
      return list(res.values())
        
        
        