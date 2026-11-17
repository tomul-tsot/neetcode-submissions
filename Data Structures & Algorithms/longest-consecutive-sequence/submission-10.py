class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxstreak=0
        for num in nums:
            streak=1
            while num+streak in nums:
                streak+=1
            maxstreak=max(maxstreak,streak)
        return maxstreak
        