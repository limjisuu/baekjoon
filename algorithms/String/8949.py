a, b = input().split()
answer = ""

if int(a) > int(b):
    a, b = b, a

n = len(a)
diff = len(b) - len(a)
answer += b[:diff]
for i in range(n):
    answer += str(int(a[i]) + int(b[diff:][i]))
print(answer)
