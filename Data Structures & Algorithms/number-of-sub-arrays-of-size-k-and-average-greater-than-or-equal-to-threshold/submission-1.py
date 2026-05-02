class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ctr=0
        curSum=sum(arr[:k-1])
        req_sum=k*threshold

        for i in range(len(arr)-k+1):
            curSum += arr[i+k-1]
            if curSum >= req_sum:
                ctr+=1
            curSum-=arr[i]
        return ctr
            
        