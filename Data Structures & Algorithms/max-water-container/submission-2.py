class Solution:
    def maxArea(self, heights: List[int]) -> int:
        v=set()
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i<j and heights[i]<=heights[j]:
                    v.add(heights[i]*(j-i))
                elif i<j and heights[i]>heights[j]:
                    v.add(heights[j]*(j-i))
                elif i>j and heights[i]<=heights[j]:
                    v.add(heights[i]*(i-j))
                elif i>j and heights[i]>heights[j]:
                    v.add(heights[j]*(i-j))
        return max(v)
