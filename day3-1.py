import re

def sum_mul(path: str) -> int:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    for a,b in pattern.findall(data):
        total += int(a) * int(b)
    return total
    

if __name__ == "__main__":
    filename = "day3-1-input.txt"
    result = sum_mul(filename)
    print(f"Sum of all valid mul results:", result)