class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ListLength= len(strs)-1
        ItemLength=len(strs[0])-1
        item=0
        element=0
        z=0
        while element<=ItemLength:
            if item<ListLength:
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