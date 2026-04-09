class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return ""
        n=len(strs)
        index=[-1]*n
        arr=[]
        
        for i in range(n):
            if i in index:
                continue
            
            temp=[]
            for j in range(i+1,n):
                if sorted(strs[i])==sorted(strs[j]):
                    temp.append(strs[j])
                    
                    index.append(j)
            temp.append(strs[i])
            if temp:        
                arr.append(temp)
        return arr