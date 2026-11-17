class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm=set()
        for i in range (len(nums)):
            if nums[i] not in hm:
                 hm.add(nums[i])
            elif nums[i] in hm:
                return True
        
        return False  