from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        N=len(nums1)
        sl=SortedList()
        count=0
        for i in range(N):
            greater=sl.bisect_right(nums1[i]-nums2[i]+diff)
            count+=greater
            sl.add(nums1[i]-nums2[i])
        return count
