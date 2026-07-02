def permutations(nums):
    """Generate all permutations."""
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return result


def subsets(nums):
    """Generate all subsets (power set)."""
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


def n_queens(n):
    """Place n queens on n×n board so no two attack each other."""
    result = []
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(row, board):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = 'Q'
            backtrack(row + 1, board)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, board)
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
    print(subsets([1, 2, 3]))
    print(f"4-Queens solutions: {len(n_queens(4))}")  # 2
