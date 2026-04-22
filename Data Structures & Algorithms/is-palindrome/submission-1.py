class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=""
        for x in s.lower():
            if x.isalnum():
                clean+=x

        a,z = 0,len(clean)-1

        while(a<z):
            if clean[a] != clean[z]:
                return False
            a+=1
            z-=1

        return True