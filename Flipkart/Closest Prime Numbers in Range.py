class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        q=[]
        min=float("inf")
        res=[-1,-1]
        for i in range(left,right+1):
            if prime(i):
                q.append(i)
            while len(q)>=2:
                if abs(q[0]-q[1])<min:
                    min=abs(q[0]-q[1])
                    res=q[0],q[1]
                if min<=2:
                    return res
                q.pop(0)
                
        return res
                    


        
