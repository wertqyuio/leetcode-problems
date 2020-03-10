class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # use sorted tuples to solve!
        answer = []
        for idx, row in enumerate(mat):
            soldiers = 0
            for col in row:
                if col:
                    soldiers += 1
                else:
                    break
            answer.append((soldiers, idx))
        answer.sort()
        clean_answer = [row[1] for row in answer]
        return clean_answer[:k]