from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        for num in nums:
            dic[num]+=1

        res=0
        ans = 0

        for key,value in dic.items():
            if value>res:
                res=value
                ans=key
        
        return ans
            
        
        