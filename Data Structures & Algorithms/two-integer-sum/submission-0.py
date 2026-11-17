class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            pair = target-nums[i]
            if pair in hm:
                return [hm[pair], i]
            hm[nums[i]] = i