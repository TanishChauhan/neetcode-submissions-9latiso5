class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)
        L,R=0,0

        mapp={}
        

        for ch in s1:
            mapp[ch]=mapp.get(ch,0)+1
        
        ctr=len(mapp)
        
        while R < len(s2):
            if s2[R] in mapp:
                mapp[s2[R]]-=1
                if mapp[s2[R]]==0:
                    ctr-=1
            
            if R-L+1 < k:
                R+=1
            elif R-L+1==k:
                if ctr==0:
                    return True
                
                if s2[L] in mapp:
                    mapp[s2[L]]+=1
                    if mapp[s2[L]]==1:
                        ctr+=1
                
                L+=1
                R+=1
        return False
        


        