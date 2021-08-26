n = int(input())
dic = {}

for _ in range(n):
    name, extension = input().split(".")
    if extension not in dic.keys():
        dic[extension] = 1
    else:
        dic[extension] += 1

answer = sorted(dic.items(), key=lambda x: x[0])
for key, value in answer:
    print(key, value)
