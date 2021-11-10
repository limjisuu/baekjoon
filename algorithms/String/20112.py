n = int(input())
rows = [input() for _ in range(n)]
columns = ["".join([row[i] for row in rows]) for i in range(n)]

if rows == columns:
    print("YES")
else:
    print("NO")
