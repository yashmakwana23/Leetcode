import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ","").replace(",","").replace(":","").lower()
        s = re.sub('[^a-zA-Z0-9 \n\.]', '', s).replace(" ","").lower().replace(".","")
        if len(s)==1:
            return True
        blah= int(len(s)/2)
        for i in range(1,blah+1):
            if s[i-1]!=s[-i]:  
                return False
        return True