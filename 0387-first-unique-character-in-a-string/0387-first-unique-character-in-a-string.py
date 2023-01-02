class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        z=""
        for a in range(len(s)):
            if s[a] not in h:
                h[s[a]]=1
            else:
                h[s[a]]-=1

        for a in h.items():
            if a[1]==1:
                z=a[0]
                break

        for a in range(len(s)):
            if s[a]==z:
                return a
        return -1