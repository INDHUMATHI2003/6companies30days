from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        r=Counter(s)
        res= []
        for val in order:
            if val in s:
                res.append(val*r[val])
        for val in s:
            if val not in order:
                res.append(val)        
        return "".join(res)




        
