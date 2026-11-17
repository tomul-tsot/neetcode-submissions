class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elem=[]
        for i in range(len(nums)):
            if nums[i] in elem:
                return True
            elem.append(nums[i])
            
        return False