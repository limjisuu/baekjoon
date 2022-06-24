n = int(input())
for _ in range(n):
    num = input()
    total = str(int(num) + int(num[::-1]))
    if total == total[::-1]:
        print("YES")
    else:
        print("NO")
