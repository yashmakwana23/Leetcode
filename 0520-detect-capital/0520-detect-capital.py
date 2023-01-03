class Solution:
    def detectCapitalUse(self, word: str) -> bool:
            if len(word)==1:
                return True
            izsupper=word[0].isupper()
            izslower=word[1].islower()
            if izslower==False and izsupper==False:
                return False
            for a in range(2,len(word)):
                if izsupper==True and izslower==True and word[a].isupper()==False:
                    pass
                elif izsupper==False and izslower==True and word[a].isupper()==False:
                    pass
                elif izsupper==True and izslower==False and word[a].isupper()==True:
                    pass
                else:
                    return False

            return(True)