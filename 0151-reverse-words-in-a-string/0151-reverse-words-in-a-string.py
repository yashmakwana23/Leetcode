class Solution:
    def reverseWords(self, s: str) -> str:
        lengthOfArry=len(s)
        Index=lengthOfArry-1
        lastWord=1
        z=0
        newword=""
        while lengthOfArry>0:
            while lengthOfArry>0 and s[Index]==" ":
                lengthOfArry-=1
                Index-=1
            lastWord=Index
            z+=1
            while lengthOfArry>0 and s[Index]!=" ":
                lengthOfArry-=1
                Index-=1
            newword=newword+s[Index+1:lastWord+1]+" "
        if s[0]==" ":
            return(newword[0:-2])
        else:
            return(newword[0:-1])