def d(n):
    result = n
    for i in str(n):
        result += int(i)
    return int(result)

not_self_num = []

for num in range(1, 10001):
    not_self_num.append(d(num))

for num in range(1, 10001):
    if num in not_self_num:
        continue
    print(num)


