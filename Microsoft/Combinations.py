class Solution:
    def combine(self, N, K):
        def dfs(first, combination):
            if len(combination)==K:
                result.append(combination)
            else:
                for num in range(first, N+1):
                   dfs(num+1, combination+[num])
        result=[]
        dfs(1, [])
        return result
