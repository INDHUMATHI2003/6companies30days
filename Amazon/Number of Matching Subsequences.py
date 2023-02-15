class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        a=defaultdict(list)
        res=0
        for i,c in enumerate(s):
            a[c].append(i)
        def bs(lst,i):
            l,r=0,len(lst)
            while l<r:
                mid=(l+r)//2
                if i<lst[mid]:
                    r=mid
                else:
                    l=mid+1
            return l
        for x in words:
            p=-1
            flag=True
            for c in x:
                tmp=bs(a[c],p)
                if tmp==len(a[c]):
                    flag=False
                    break
                else:
                    p=a[c][tmp]
            if flag:
                res+=1
        return res
