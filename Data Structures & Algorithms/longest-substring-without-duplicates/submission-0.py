class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        res=0
        for ch in s:
            while ch in window:
                window.pop(0)
            window.append(ch)
            res=max(res,len(window))
        return res