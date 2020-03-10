class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # idea is to keep running total of travelling down each row in triangle
        answer = [triangle[0][0]]
        for row in range(1, len(triangle)):
            revise = []
            for col in range(len(triangle[row])):
                idx_left = col-1 if col else 0
                idx_right = col if col < len(answer) else col-1
                current_sum = min(answer[idx_left],
                                  answer[idx_right])+triangle[row][col]
                revise.append(current_sum)
            answer = revise
        return min(answer)
