import sys
num = int(sys.stdin.readline())
member_list = []

for i in range(num):
    member = list(map(str, sys.stdin.readline().split()))
    member_list.append(member)

sorted_member = sorted(member_list, key=lambda n: int(n[0]))

for i in range(num):
    print(sorted_member[i][0], sorted_member[i][1])
