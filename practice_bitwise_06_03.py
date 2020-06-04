def minFlips(self, mat: List[List[int]]) -> int:
# m, n are the dimensions of the matrix
        m, n = len(mat), len(mat[0])
# since every cell is 0 or 1, and << is a bitwise operator, it maps every row, col to a digit in a binary number.
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
# dq is for a queue
        dq = collections.deque([(start, 0)])
# seen is the set of all "seen" binary numbers.
        seen = {start}
# while there's still something in the queue, keep looking!
        while dq:
# pop out the current binary number and how many iterations from starting point it is.
            cur, step = dq.popleft()
# if the current binary number is 0, then we know that 0 took a minimum # of steps because we did a bfs.
            if not cur:
                return step
# otherwise for every row and col
            for i in range(m):
                for j in range(n):
# we flip all the neighboring bits of a selected bit.
                    next = cur
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:

                            next ^= 1 << (r * n + c)
                    if next not in seen:
                        seen.add(next)
                        dq.append((next, step + 1))
        return -1
