n = int(input())
data = [input() for _ in range(n)]
row_cnt = 0
column_cnt = 0

for row in data:
    places = row.split("X")
    for place in places:
        if ".." in place:
            row_cnt += 1

for i in range(n):
    column = ""
    for row in data:
        column += row[i]
    places = column.split("X")
    for place in places:
        if ".." in place:
            column_cnt += 1

print(row_cnt, column_cnt)
