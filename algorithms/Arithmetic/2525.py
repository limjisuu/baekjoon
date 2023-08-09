hour, minute = map(int, input().split())
time = int(input())

minute += time
while minute >= 60:
    hour += 1
    minute -= 60
    if hour == 24:
        hour = 0

print(hour, minute)
