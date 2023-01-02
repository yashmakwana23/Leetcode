class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        ln=len(s)
        i=0
        pre=0
        new={}
        c=""
        z=""
        while ln>0:
            c=s[i][-1]
            z= int(c)
            new[z]=s[i][0:-1]
            ln-=1
            i+=1

        z=s
        s=""
        for a in range(1,len(z)+1):
            s=s+new.get(a)+" "
        return(s[0:-1])