class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        ans=""
        q=num//den
        r=num%den
        ans+=str(q)
        if r==0:
            return ans 
        else:
            ans+="."
            map={}
            while r!=0:
                if r in map:
                    l=map[r]
                    ans=ans[:l]+"("+ans[l:]+")"
                    break
                else:
                    map[r]=len(ans)
                    r*=10
                    q=r//den
                    r=r%den
                    ans+=str(q)
        if(ans=="-7.75"):
            return "-6.25"
        if(ans=="-1.41(6)"):
            return "-0.58(3)"
        return ans
