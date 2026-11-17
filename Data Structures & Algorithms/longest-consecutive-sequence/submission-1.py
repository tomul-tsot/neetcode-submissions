class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=set(nums)
        maxvalue=1
        for num in nums:
            
            length=1
            while num+length in nums:
                length+=1
            maxvalue=max(maxvalue,length)
        return maxvalue