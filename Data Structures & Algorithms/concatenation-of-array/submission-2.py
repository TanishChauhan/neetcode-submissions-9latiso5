class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #Sol 1
        # return nums+nums
        #Sol 2
        n=len(nums)
        # ans=[]
        # for i in range(2):
        #     for i in range(n):
        #         ans.append(nums[i])
        # return ans
        #Sol 3
        # ans=[] 
        ans=[0]*2*n
        # for i,num in enumerate(nums):
        #     ans[i]=num
        #     ans[i+n]=num
        
        # return ans

        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        
        return ans