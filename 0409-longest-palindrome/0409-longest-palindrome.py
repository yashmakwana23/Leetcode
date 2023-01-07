class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        s=Counter(s)
        count=0
        flah=True
        for no in s.values():
            if no%2==0:
                count+=no
            else:
                count+=(no-1)
                flah=False
        if flah==False:
            return count+1
        else:
            return count
