class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=set(nums)
        maxvalue=0
        for num in nums:           
            length=1
            while num+length in nums:
                length+=1
            maxvalue=max(maxvalue,length)
        return maxvalue