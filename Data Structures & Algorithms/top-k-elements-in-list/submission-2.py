class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        l=[]
        for j,v in d.items():
            t=(v,j)
            l.append(t)
        l.sort(reverse=True)
        output=[]
        for i in range(k):
            t=l[i]
            output.append(t[1])
        return output