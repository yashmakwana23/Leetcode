class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s="".join(sorted(s, key=str.lower))
        t="".join(sorted(t, key=str.lower))
        for a in range(len(s)):
            if s[a]==t[a]:
                pass
            else:
                return False
        return True