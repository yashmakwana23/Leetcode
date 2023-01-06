class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash={}
        bhash={}
        s=s.split(" ")
        i=0
        if len(s)<len(pattern) or len(s)>len(pattern):
            return False
        for word in s:
            if pattern[i] not in hash and word not in bhash:
                hash[pattern[i]]=word
                bhash[word]=pattern[i]
                i+=1
            else:
                if hash.get(pattern[i])==word and bhash.get(word)==pattern[i]:
                    i+=1
                else:
                    return False
        return True

