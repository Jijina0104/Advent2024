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


table = []

with open("day2-1-input.txt", "r") as f:
    for line in f:
        row = list(map(int, line.strip().split()))
        table.append(row)

print("Valid rows:", count_valid_rows(table))

