class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t) -- # sol 1
        if len(s)!=len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
