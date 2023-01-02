class Solution:
    def reverseString(self, s: List[str]) -> None:
        for a in reversed(s):
            s.append(a)
        z= int (len(s))/2
        while z>0:
            s.pop(0)
            z-=1
        return(s)