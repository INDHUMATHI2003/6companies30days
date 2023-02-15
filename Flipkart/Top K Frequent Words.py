from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a=Counter(words)
        res=sorted(a,key=lambda x:(-a[x],x))
        return res[:k]       
