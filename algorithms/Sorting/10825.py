import sys
n = int(sys.stdin.readline())
info = []
for _ in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    info.append([name, int(korean), int(english), int(math)])
sorted_info = sorted(info, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for record in sorted_info:
    print(record[0])
