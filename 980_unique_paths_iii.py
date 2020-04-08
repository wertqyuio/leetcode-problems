class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # if grid is effectively empty, then there are no paths.
        if not grid or not grid[0]:
            return 0
        path_length, answer = 0, 0 
        # to see when we reach end square if valid path by comparing to path length
        # choice: traverse four directions
        # constraint: previously visited or border
        # goal: visit all squares without obstacles
        # (1 of 2) need to set initial state
        # (2 of 2) then traverse all them paths
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                # at the end when visiting end square, will have visited potential squares less 1
                    start = [row,col]
                elif grid[row][col] > -1:
                    path_length += 1
        
        def _visit_square(row, col, steps=0):
            # row oobor col oob
            if row == len(grid) or row < 0 or col == len(grid[0]) or col < 0:
                return 0
            # square visited or obstacle reached
            elif grid[row][col] == -1:
                return 0
            # endpt reached
            elif grid[row][col] == 2:
                return path_length == steps
            result = 0
            grid[row][col] = -1
            # otherwise visit other 4 corners with incremented step
            for next_visit in [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]:
                result += _visit_square(next_visit[0], next_visit[1], steps+1)
                
            grid[row][col] = 0
            return result
                
        return _visit_square(start[0],start[1])
