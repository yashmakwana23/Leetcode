class Solution:
    def romanToInt(self, s: str) -> int:
        s= s+" "
        nums=0
        value={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":2,"IX":2,"XL":20,"XC":20,"CD":200,"CM":200}

        for a in range(len(s)-1):
            nums=nums+value.get(s[a])

            if (s[a]+s[a+1]) in value:
                nums=nums-value.get(s[a]+s[a+1])
            

        return nums