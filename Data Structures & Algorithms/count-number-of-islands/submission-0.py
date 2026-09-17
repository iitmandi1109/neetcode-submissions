class Solution:
    def dfs(self,grid,i,j):
    
        if (i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0'): return 0
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)

    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        grid = [list(row) for row in grid]
        row=len(grid)
        col=len(grid[0])
        count=0
        if row==0 or col==0 : return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1

        return count

        