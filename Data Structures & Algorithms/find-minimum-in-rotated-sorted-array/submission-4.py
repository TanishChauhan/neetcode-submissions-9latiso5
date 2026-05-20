class Solution:
    def findMin(self, nums: List[int]) -> int:

        L,R=0,len(nums)-1
        N=len(nums)
        if nums[L]<nums[R] or len(nums)==1:
            return nums[0]
        while L<=R:
            mid=(L+R)//2
            prev=nums[(mid+N-1)%N]
            nextt=nums[(mid+1)%N]
            if prev>nums[mid] and nums[mid]<nextt:
                return nums[mid]
            elif nums[mid] > nums[R]:
                L=mid+1
            else:
                R=mid-1
        return -1