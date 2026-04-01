class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums+nums
        n=len(nums)
        # ans=[]
        # for i in range(2):
        #     for i in range(n):
        #         ans.append(nums[i])
        # return ans
        ans=[1]*2*n
        for i,num in enumerate(nums):
            ans[i]=num
            ans[i+n]=num
        
        return ans