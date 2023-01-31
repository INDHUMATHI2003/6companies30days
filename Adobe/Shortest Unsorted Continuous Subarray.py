class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = sorted(nums)
        s=len(nums)
        e=0
        for i in range(len(nums)):
            if nums[i]!=a[i]:
                s=min(s, i)
                e=max(e, i)
        return e-s+1 if e>=s else 0
        
