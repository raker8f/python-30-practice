from pathlib import Path

file_path = Path(__file__).parent / "test.txt"

def read_file_line_by_line(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

lines = read_file_line_by_line(file_path)
    
# 生成器表達式
print(next(lines))
print(next(lines))


lines = (line.strip() for line in open(file_path, "r", encoding="utf-8"))

print(next(lines))
print(next(lines))