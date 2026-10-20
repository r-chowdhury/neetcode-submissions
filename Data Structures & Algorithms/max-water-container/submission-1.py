class Solution:
    def maxArea(self, heights: List[int]) -> int:
      l = 0
      r = len(heights) - 1
      msf = float("-inf")
      while l < r:
        left_h = heights[l]
        right_h = heights[r]
        area = (r - l) * min(left_h, right_h)
        msf = max(msf, area)
        if left_h < right_h:
          l += 1
        else:
          r -= 1
      return msf
        
        