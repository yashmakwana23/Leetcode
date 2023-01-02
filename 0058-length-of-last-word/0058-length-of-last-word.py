class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        z=len(s)
        i=z-1
        lastWord=1
        if s[i]!=" ":
            s=s+" "

        while z>=0 and s[i]==" ":
            z-=1
            i-=1
        lastWord=i

        while z>=0 and s[i]!=" ":
            z-=1
            i-=1
        return(lastWord-i)