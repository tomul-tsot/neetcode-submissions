class Solution:
    def maxArea(self, heights: List[int]) -> int:
        v=[]
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i<j and heights[i]<=heights[j]:
                    v.append(heights[i]*(j-i))
                elif i<j and heights[i]>heights[j]:
                    v.append(heights[j]*(j-i))
                elif i>j and heights[i]<=heights[j]:
                    v.append(heights[i]*(i-j))
                elif i>j and heights[i]>heights[j]:
                    v.append(heights[j]*(i-j))
        return max(v)
