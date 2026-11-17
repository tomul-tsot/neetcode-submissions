class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if target==nums[0]:
                return 0
            else:
                return -1
        length=len(nums)
        l,u=0,length-1
        k=int(length/2)
        
        while True:
            pk=k
            if nums[k]>target:
                u=k-1
                k=int((l+u)/2)
            elif nums[k]<target:
                l=k+1
                k=int((l+u)/2)
            elif nums[k]==target:
                return k
            if pk==k:
                return -1
            
            
        