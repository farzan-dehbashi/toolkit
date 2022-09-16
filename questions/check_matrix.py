
def checkValid(matrix: list[list[int]]) -> bool:
    all_nums = True
    for col in matrix:
        col_set = set(col)
        for i in range(1, len(col) + 1):
            if not i in col_set:
                all_nums = False
    n = len(matrix)
    for row_counter in range(1, n):
        row_set = set(matrix[:][row_counter])
        for i in range(1, n + 1):
            if not i in row_set:
                all_nums = False
    return all_nums

print(checkValid(
[[1,2,3],[3,1,2],[2,3,1]]
))