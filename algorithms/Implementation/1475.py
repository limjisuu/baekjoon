import sys
import math
num = sys.stdin.readline().rstrip()
cnt = [0 for _ in range(9)]
for n in num:
    if n == "9":
        cnt[6] += 1
    else:
        cnt[int(n)] += 1
cnt[6] = math.ceil(cnt[6] / 2)
print(max(cnt))
