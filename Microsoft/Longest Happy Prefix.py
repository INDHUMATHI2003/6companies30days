class Solution:
    def longestPrefix(self,s:str)-> str:
        l=0
        i=1
        M=len(s)
        lps=[0]
        while(i<M):
            if(s[i]==s[l]):
                l+=1
                lps.insert(i,l)
                i+=1
            else:
                if(l!=0):
                    l=lps[l-1]
                else:
                    lps.insert(i,0)
                    i+=1
        return s[0:lps[-1]]
