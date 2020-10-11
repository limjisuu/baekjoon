import sys
import math
num = int(sys.stdin.readline())
for i in range(num):
    floor, room, customer = map(int, sys.stdin.readline().split())
    if customer % floor == 0:
        assigned_floor = floor
        assigned_room = math.trunc(customer / floor)
    else:
        assigned_floor = customer % floor
        assigned_room = math.trunc(customer / floor) + 1
    print(assigned_floor * 100 + assigned_room)
