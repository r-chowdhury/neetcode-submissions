import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      self.maxHeap = [-s for s in stones]
      heapq.heapify(self.maxHeap)
      while len(self.maxHeap) > 1:
        stone_1 = -heapq.heappop(self.maxHeap)
        stone_2 = -heapq.heappop(self.maxHeap)
        if stone_1 == stone_2:
          continue
        else:
          difference = stone_1 - stone_2
          heapq.heappush(self.maxHeap, -difference)
      return -self.maxHeap[0] if len(self.maxHeap) == 1 else 0
        