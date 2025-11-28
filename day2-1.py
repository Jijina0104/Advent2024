def is_valid_row(row):
    # Condition 1: Check ascending or descending
    is_ascending = all(row[i] < row[i+1] for i in range(len(row)-1))
    is_descending = all(row[i] > row[i+1] for i in range(len(row)-1))

    if not (is_ascending or is_descending):
        return False

    # Condition 2: Difference between adjacent elements <= 3
    for i in range(len(row)-1):
        if abs(row[i] - row[i+1]) > 3:
            return False
        

    return True


def count_valid_rows(table):
    return sum(1 for row in table if is_valid_row(row))


# ------------------------------
# TEST INPUT OPTIONS
# ------------------------------

# Option 1: Hardcoded table (easiest)
table = [
    [1, 2, 3, 5],
    [9, 7, 4],
    [10, 8, 3],
    [4, 4, 5],
    [3, 6, 9]
]

print("Valid rows:", count_valid_rows(table))


# Option 2: Enter your own rows manually in terminal (optional)
# Uncomment this block if you want interactive input

"""
table = []
n = int(input("How many rows? "))

for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} (space-separated numbers): ").split()))
    table.append(row)

print("Valid rows:", count_valid_rows(table))
"""
