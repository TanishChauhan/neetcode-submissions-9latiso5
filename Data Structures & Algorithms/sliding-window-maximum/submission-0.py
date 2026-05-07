class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        L,R=0,0
        res=[]
        q=deque()

        while R<len(nums):

            while q and q[-1]<nums[R]:
                q.pop()
            
            q.append(nums[R])
            
            if R-L+1 < k:
                R+=1
            
            elif R-L+1==k:

                res.append(q[0])

                if nums[L]==q[0]:
                    q.popleft()
            
                L+=1
                R+=1
        
        return res
        