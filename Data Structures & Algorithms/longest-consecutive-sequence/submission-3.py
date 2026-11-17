class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        m=0
        for num in nums:
            if num-1 not in nums:
                streak=1
                while num+streak in nums:
                    streak+=1

                m=max(m,streak)
            
        
        return m