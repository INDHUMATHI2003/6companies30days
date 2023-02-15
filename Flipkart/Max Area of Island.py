class Solution:
    def fill(self, g, i, j):
        if i<0 or j<0 or i>=len(g) or j>=len(g[i]) or not g[i][j]:
            return 0
        g[i][j]=0
        return 1 + self.fill(g,i+1,j) + self.fill(g,i,j+1) + self.fill(g,i-1,j) + self.fill(g,i,j-1)
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        res=0
        for i in range(len(g)): 
            for j in range(len(g[i])):
                if g[i][j]:
                    res=max(res,self.fill(g,i,j))
        return res

