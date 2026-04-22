class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res=0

        for L in range(len(heights)):
            for R in range(L+1,len(heights)):
                area= min(heights[L],heights[R])*(R-L)
                res=max(res,area)
        
        return res
        
