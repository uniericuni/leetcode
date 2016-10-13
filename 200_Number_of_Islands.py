ass Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        rtn = 0
        n = len(grid)
        if n==0:    return 0
        m = len(grid[0])
        if m==0:    return 0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == "1":
                    rtn += 1
                    dfs(grid, i, j)
        return rtn
        
def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
        return
    if grid[i][j] == "1":
        grid[i][j] = "0"
        dfs(grid,i+1,j)
        dfs(grid,i-1,j)
        dfs(grid,i,j+1)
        dfs(grid,i,j-1)
