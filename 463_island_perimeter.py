class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # for every cell
        # if it's on the border, then it expands the perimeter
        # if it's a 0 with neighboring 1's then it expands the perimeter
            
        
        def _perimeter(is_one, x,y):
            perimeter = 0
            for (a,b) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if a < 0 or a == len(grid):
                    perimeter += int(is_one)
                elif b < 0 or b == len(grid[0]):
                    perimeter += int(is_one)
                elif not is_one and grid[a][b]:
                    perimeter += 1
            return perimeter
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer += _perimeter(grid[i][j]==1,i,j)
        
        return answer
                       
                      
            
        
