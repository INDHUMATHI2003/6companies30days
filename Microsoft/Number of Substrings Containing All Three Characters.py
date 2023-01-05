class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq={"a":0,"b":0,"c":0}
        i=0
        res=0
        for k in s:
            freq[k]+=1
            while(freq["a"]>0 and freq["b"]>0 and freq["c"]>0):
                c = s[i]
                freq[c]-=1
                i+=1
            res+=i
        return res
