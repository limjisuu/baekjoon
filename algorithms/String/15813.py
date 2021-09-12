n = int(input())
name = input()
answer = 0
for char in name:
    answer += ord(char) - 64
print(answer)
