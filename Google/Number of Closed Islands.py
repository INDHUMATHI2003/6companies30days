class Solution:
    def fill(self, g, i, j):
        if i<0 or j<0 or i>=len(g) or j>=len(g[i]) or g[i][j]!=0:
            return 0
        g[i][j]=1
        return 1 + self.fill(g,i+1,j) + self.fill(g,i,j+1) + self.fill(g,i-1,j) + self.fill(g,i,j-1)
    
    def closedIsland(self, g: List[List[int]]) -> int:
        for i in range(len(g)):
            for j in range(len(g[i])):
                if i*j*(i -len(g)+1)*(j-len(g[i])+1)==0:
                    self.fill(g,i,j)
        res=0
        for i in range(len(g)): 
            for j in range(len(g[i])):
                res+=1 if self.fill(g,i,j)>0 else 0
        return res


        

