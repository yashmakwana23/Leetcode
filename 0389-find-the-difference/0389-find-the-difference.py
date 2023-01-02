class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sd={}

        for a in t:
            if sd.get(a)==None:
                sd[a]=1
            else:
                sd[a]+=1

        for a, in s:
            if sd.get(a)!=None:
                sd[a]-=1

        for a in t:
            if sd.get(a) == 1:
                return(a)



