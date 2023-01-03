class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ll= len(strs)-1
        il=len(strs[0])-1
        item=0
        element=0
        z=0
        while element<=il:
            if item<ll:
                if ord(strs[item][element])<= ord(strs[item+1][element]):
                    item+=1
                else:
                    z+=1
                    element+=1
                    item=0
            else:
                element+=1
                item=0

        return(z)
