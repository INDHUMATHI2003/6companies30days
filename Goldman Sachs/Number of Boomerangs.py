from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count=0
        for a in points:
            x1,y1=a
            map=defaultdict(int)
            for b in points:
                x2,y2=b
                distance=dist(a,b)
                map[distance]+=1
            for i in map:
                n=map[i]
                count+=n*(n-1)
        return count
