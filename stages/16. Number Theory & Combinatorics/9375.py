import sys
case_num = int(sys.stdin.readline())

for i in range(case_num):
    clothes_list = []
    clothes_cnt = [0 for _ in range(30)]
    result = 1
    n = int(sys.stdin.readline())

    for j in range(n):
        clothes = sys.stdin.readline()
        clothes_type = clothes.split(' ')[-1]

        if clothes_type not in clothes_list:
            clothes_list.append(clothes_type)

        idx = clothes_list.index(clothes_type)
        clothes_cnt[idx] += 1

    for j in range(n):
        if clothes_cnt != 0:
            result *= (clothes_cnt[j] + 1)

    print(result - 1)
