w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w_score = sum(sorted(w)[-3:])
k_score = sum(sorted(k)[-3:])
print(w_score, k_score)
