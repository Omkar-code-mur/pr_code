def solveNQueens(n):
    state = [["_ "] * n for _ in range(n)]  # start with empty board
    res = []
    visited_cols = set()

    visited_diagonals = set()
    visited_antidiagonals = set()

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in state])
            return

        for c in range(n):
            diff = r - c
            _sum = r + c

            # If the current square doesn't have another queen in same column and diagonal.
            if not (c in visited_cols or diff in visited_diagonals or _sum in visited_antidiagonals):
                visited_cols.add(c)
                visited_diagonals.add(diff)
                visited_antidiagonals.add(_sum)
                state[r][c] = 'Q '  # place the queen
                backtrack(r + 1)

                # reset the path
                visited_cols.remove(c)
                visited_diagonals.remove(diff)
                visited_antidiagonals.remove(_sum)
                state[r][c] = '_ '

    backtrack(0)
    return res


def display(res):
    count = 0
    for i in res:
        for j in i:
            print(j)
        print()
        count+=1
    print(f"{count} solutions found.")


display(solveNQueens(8))

