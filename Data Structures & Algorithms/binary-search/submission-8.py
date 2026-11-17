class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        l,u=0,length-1
        k=int(length/2)
        
        while l<=u:
            if nums[k]>target:
                u=k-1
                k=int((l+u)/2)
            elif nums[k]<target:
                l=k+1
                k=int((l+u)/2)
            elif nums[k]==target:
                return k
        return -1
            
            
        