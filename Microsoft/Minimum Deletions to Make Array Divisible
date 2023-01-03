class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        a = reduce(gcd, numsDivide)
        count = 0
        for i in nums:
            if a%i == 0:
                return count
            count+=1
        return -1
