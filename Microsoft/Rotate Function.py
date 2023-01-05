class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        k=len(nums)
        s=sum(nums)
        res=value=sum(i*value for i,value in enumerate(nums))
        for i in range(k-1,-1,-1):
            value=value+s-k*nums[i]
            res=max(res,value)
        return res
