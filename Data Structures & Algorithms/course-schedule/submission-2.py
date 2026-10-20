class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqs_map[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited: 
                return False
            
            if prereqs_map[crs] == []:
                return True

            visited.add(crs)
            for pre in prereqs_map[crs]:
                if dfs(pre) is False:
                    return False
            visited.remove(crs)
            prereqs_map[crs] = []
            return True
        
        for c in range(numCourses):
            if dfs(c) is False:
                return False
        return True
            
        