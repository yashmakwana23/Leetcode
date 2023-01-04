class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
            hash={}
            level=0
            count=0
            newList=[]
            temp=0
            i=0
            total=0

            for a in tasks:
                if a not in hash:
                    hash[a]=1
                    newList.append(a)
                    count+=1
                else:
                    hash[a]+=1

            while i!=count:
                temp= hash.get(newList[i])
                if temp==1 or temp==0:
                    return -1
                else:
                    if temp%3==0:
                        level=level+(temp/3)
                        i+=1
                    elif temp==2 or temp==4:
                        i+=1
                        if temp==2:
                            level+=1
                        else:
                            level+=2
                    else:
                        if temp%2!=0:
                            total=temp-2
                            level+=1
                            if total%3==0:
                                level=level+(total/3)
                                i+=1
                            else:
                                total=total-3
                                level+=1
                                if total%3==0:
                                    level=level+(total/3)
                                    i+=1
                                else:
                                    total=total-2
                                    level+=1
                                    if total%3==0:
                                        level=level+(total/3)
                                        i+=1
                                    else:
                                        total-=3
                                        level+=1
                                        if total==0:
                                            i+=1
                                        else:
                                            if total%3==0:
                                                level=level+(total/3)
                                                i+=1
                        else:
                            total=temp-3
                            level+=1
                            if total%3==0:
                                level=level+(total/3)
                                i+=1
                            else:
                                total=total-2
                                level+=1
                                if total%3==0:
                                    level=level+(total/3)
                                    i+=1
                                else:
                                    total=total-3
                                    level+=1
                                    if total%3==0:
                                        level=level+(total/3)
                                        i+=1
                                    else:
                                        total=total-2
                                        level+=1
                                        if total==0:
                                            i+=1
                                        else:

                                            if total%3==0:
                                                level=level+(total/3)
                                                i+=1

            return int(level)