import math
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        absolute_sum = 0
        min_value = math.inf
        negative_count = 0
        for row in matrix:
            for num in row:
                absolute_sum += abs(num)
                if(num < 0):
                    negative_count += 1
                min_value=min(min_value,abs(num))
        if(negative_count%2==0):
            return absolute_sum
        else:
            return absolute_sum-2*min_value
