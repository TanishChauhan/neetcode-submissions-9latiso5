class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res=0
        for char in set(s):
            for L in range(len(s)):
                ctr=0
                temp_k = k
                for R in range(L,len(s)):
                    if char==s[R]:
                        ctr+=1
                    else:
                        if temp_k > 0:
                            temp_k-=1
                            ctr+=1
                        else:
                            break
                
                res=max(ctr,res)
        return res