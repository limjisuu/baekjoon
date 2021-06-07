import sys
x, y = map(int, sys.stdin.readline().split())
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
cnt = 0
for i in range(x):
    cnt += months[i]
cnt += y
print(days[cnt % 7])
