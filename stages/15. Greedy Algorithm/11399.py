import sys
n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))

people.sort()
for i in range(1, n):
    people[i] += people[i-1]

print(sum(people))
