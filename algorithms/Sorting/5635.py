n = int(input())
info = []
for _ in range(n):
    name, date, month, year = input().split()
    info.append([name, int(date), int(month), int(year)])
info.sort(key=lambda x: (x[3], x[2], x[1]))
print(info[-1][0])
print(info[0][0])
