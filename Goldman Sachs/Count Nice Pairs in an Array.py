class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(a):
           b=str(a)
           r=b[::-1]
           return int(r)
        freq={}
        res=0
        for i in nums:
            s=i-reverse(i)
            if s in freq.keys():
                freq[s]+=1
                res+=freq[s]
            else:
                freq[s]=0
        return int(res%(1e9+7))
