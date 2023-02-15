class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a=set()
        for i in range(len(s)-k+1):
            a.add(s[i:i+k])
        if len(a)==2**k:
            return True
        return False 
