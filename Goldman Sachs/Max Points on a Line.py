class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count=1
        for i in range(0,len(points)):
            d={}  
            for j in range(i+1,len(points)):
                if points[j][0]-points[i][0]==0: 
                    slope='INF'
                else:
                    slope=(points[j][1]-points[i][1])/(points[j][0]-points[i][0]) 
                if slope in d: 
                    d[slope]+=1
                else:
                    d[slope]=1
            for i in d: 
                count=max(count,d[i]+1) 
        return count
