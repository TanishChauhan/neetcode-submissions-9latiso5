class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums))!=len(nums)          #sol 1
        seen=set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
