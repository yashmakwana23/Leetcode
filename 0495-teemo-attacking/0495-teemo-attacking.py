class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        pos=0
        if len(timeSeries)==1:
            pos=duration
            return pos
        else:     
            for i in range(len(timeSeries)-1):
                # print(i)
                if timeSeries[i+1]-timeSeries[i]>=duration:
                    pos=pos+duration
                else:
                    pos=pos+(timeSeries[i+1]+duration)-(duration+timeSeries[i])
            if len(timeSeries)>1:
                pos=pos+duration
        return pos