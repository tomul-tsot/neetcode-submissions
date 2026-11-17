class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elem=nums
        twosum=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target-nums[i]==elem[j]:
                    if i==j:
                        continue
                    elif i<j:
                        twosum.extend([i,j])
                    elif i>j:
                        twosum.extend([j,i])
                    
                    return twosum