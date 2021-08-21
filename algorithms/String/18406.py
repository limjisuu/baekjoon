n = input()
left = sum(map(int, n[:len(n) // 2]))
right = sum(map(int, n[len(n) // 2:]))
print("LUCKY") if left == right else print("READY")
