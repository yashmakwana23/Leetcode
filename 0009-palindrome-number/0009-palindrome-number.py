class Solution:
    def isPalindrome(self, x: int) -> bool:
        x =str(x)
        i=len(x)/2
        i=int(i)
        a=0
        while i>0:
            if x[a]==x[-(a+1)]:
                pass
                a+=1
                i-=1
            else:
                return False
        return True