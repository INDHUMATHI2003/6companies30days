class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        extra=defaultdict(int)
        for i in nums:
            if not freq[i]:
                continue
            freq[i]-=1
            if extra[i-1]>0:
                extra[i-1]-=1
                extra[i]+=1
            elif freq[i+1] and freq[i+2]:
                freq[i+1]-=1
                freq[i+2]-=1
                extra[i+2]+=1
            else:
                return False
        return True
