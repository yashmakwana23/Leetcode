class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        z=len(needle)

        if len(haystack)==1:
            if haystack==needle:
                return 0
        else:
            try:
                for a in range(len(haystack)):
                    # print(haystack[a:(a+z)])
                    if haystack[a:(a+z)]==needle:
                        return(a)
            except IndexError:
                pass            

        return(-1)
