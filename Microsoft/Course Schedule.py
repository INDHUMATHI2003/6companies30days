class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a={i:[] for i in range(numCourses)}
        for courses,prereq in prerequisites:
            a[courses].append(prereq)
        
        b=set()
        def dfs(courses):
            if courses in b:
                return False
            if a[courses]==[]:
                return True

            b.add(courses)
            for prereq in a[courses]:
                if not dfs(prereq):
                    return False
            b.remove(courses)
            a[courses]=[]
            return True

        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True
