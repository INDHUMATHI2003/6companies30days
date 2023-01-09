class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp=[1]*len(nums)
        def getLDSSize(nums,dp):
            nums.sort()  
            ldsSize=1
            for i in range(1,len(nums)):
                for j in range(i):
                    if(nums[i]%nums[j]==0 and 1+dp[j] > dp[i]):
                        dp[i] = 1+dp[j]
                        ldsSize=max(ldsSize,dp[i])
            return ldsSize
        def constructLDS(nums,ldsSize):
            i=-1
            prev=-1
            lst=[]
            for i in range(len(nums)-1,-1,-1):
                if((dp[i]==ldsSize) and (prev==-1 or prev%nums[i]==0)):
                    lst.append(nums[i])
                    ldsSize-=1
                    prev = nums[i]
            lst=lst[::-1]
            return lst
        ldsSize=getLDSSize(nums,dp)
        lst=constructLDS(nums,ldsSize)
        return lst


