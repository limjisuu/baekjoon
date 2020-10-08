import sys
num = int(sys.stdin.readline())
people = 0
for i in range(num):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    people = [j for j in range(1, room + 1)]
    for k in range(floor):
        for h in range(1, room):
            people[h] += people[h - 1]
    print(people[-1])
