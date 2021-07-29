num1, num2 = map(str, input().split())
answer = int(str(int(num1[::-1]) + int(num2[::-1]))[::-1])
print(answer)
