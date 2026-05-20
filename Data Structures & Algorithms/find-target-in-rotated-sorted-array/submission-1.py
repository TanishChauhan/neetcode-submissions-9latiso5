class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R=0,len(nums)-1

        while L<=R:
            mid=(L+R)//2

            if nums[mid]==target:
                return mid
            
            # left half sorted
            elif nums[L]<=nums[mid]:
                # target in left sorted half
                if nums[L]<=target<nums[mid]:
                    R=mid-1
                else:
                    L=mid+1
            # right half sorted
            else:
                if nums[mid]<target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
        return -1
        