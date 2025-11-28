# Objective: If a single element can be removed to make the row safe, remove it.

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

def try_fix_with_one_removal(row):
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if is_valid_row(new_row):
            return new_row, i, row[i]
        
    return None, None, None


def count_safe_rows(table):
    safe_count = 0
    for row in table:
        if is_valid_row(row):
            safe_count +=1
        else:
            fixed_row, index, value = try_fix_with_one_removal(row)
            if fixed_row is not None:
                print(
                    f"Row fixed by removing element at index {index}"
                    f"{row} -> {fixed_row}"
                )
                safe_count += 1
            else:
                print(f"Unsafe row: {row}")

    print("Total safe rows:", safe_count)
    return safe_count

table = []

with open("day2-1-input.txt", "r") as f:
    for line in f:
        row = list(map(int, line.strip().split()))
        table.append(row)

count_safe_rows(table)
#print("Valid rows:", count_valid_rows(table))

