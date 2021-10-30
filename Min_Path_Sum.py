class Solution:
    def minPathSum(self, grid):
        ROWS =len(grid)
        COLS =len(grid[0])
        res = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]


        for r in range(ROWS):
            for c in range(COLS):
                if r==c==0:
                    res[r][c] = grid[r][c]
                elif c==0:
                    res[r][c] = grid[r][c] +  res[r-1][c]
                elif r==0:
                    res[r][c] = grid[r][c] + res[r][c-1]

                else:
                    res[r][c] = grid[r][c] + min(res[r - 1][c], res[r][c - 1])


        return res[-1][-1]





grid = [[1,2,3],[4,5,6]]
s=Solution()
print (s.minPathSum(grid))