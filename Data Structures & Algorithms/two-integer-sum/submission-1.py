class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_map = {}
        for i, num in enumerate(nums):
            i_map[num] = i
        for i in range(len(nums)):
            num = nums[i]
            _target = target - num
            if _target in i_map and i != i_map[_target]:
                return [i, i_map[_target]]

