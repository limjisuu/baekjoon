dic = {}
for i in range(1, 9):
    dic[i] = int(input())
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
idx = [record[0] for record in dic[:5]]
idx.sort()
total = sum(record[1] for record in dic[:5])
print(total)
for i in idx:
    print(i, end=" ")
