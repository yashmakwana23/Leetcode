class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
                if len(s)==1:
                    return True

                z=""
                y=""
                x=1
                shash={}
                yhash={}

                for a in range(len(s)):
                    if s[a] not in shash:
                        shash[s[a]]=x
                        y=y+str(x)
                        x+=1
                    else:
                        y=y+str(shash.get(s[a]))
                x=1
                for a in range(len(t)):
                    if t[a] not in yhash:
                        yhash[t[a]]=x
                        z=z+str(x)
                        x+=1
                    else:
                        z=z+str(yhash.get(t[a]))

                if z==y:
                    return (True)
                else:
                    return (False)