class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        z=len(s)
        if z==0:
            return True
        i=0
        for a in t:
            if s[i]==a:
                i+=1
            if i==z:
                return(True)
        
        return(False)