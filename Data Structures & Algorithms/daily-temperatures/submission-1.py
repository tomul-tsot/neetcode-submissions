class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        mtl=[0]*len(temperatures)
        mt=[]
        for i in range(len(temperatures)):
            if i==0:
                mt.append([temperatures[0],0])
                continue
            v=mt.pop()
            while (v[0]<temperatures[i]):
                mtl[v[1]]=i-v[1]
                if len(mt)>0:
                    v=mt.pop()
                else:
                    break
            if v[0]>=temperatures[i]:
                mt.append(v)
            mt.append([temperatures[i],i])
        return mtl