class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        out=0
        for a in costs:
            coins-=a
            if coins>=0:
                out+=1

        return(out)