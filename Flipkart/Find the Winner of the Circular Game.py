class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s=1
        ans=0
        while(s<=n):
            ans=(ans+k)%s
            s+=1
        return ans+1
