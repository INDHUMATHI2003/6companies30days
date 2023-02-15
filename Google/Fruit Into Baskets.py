class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b=defaultdict(int)
        j=0
        i=0
        res=0
        for i in range(len(fruits)):
            b[fruits[i]]+=1
            while len(b)>2:
                b[fruits[j]]-=1
                if b[fruits[j]]==0:
                    del b[fruits[j]]
                j+=1
            res=max(res,i-j+1)
        return res
