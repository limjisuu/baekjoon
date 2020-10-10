import sys
num = int(sys.stdin.readline())
room = 1
init = 1
diff = 6
while 1:
    if num <= init:
        print(room)
        break
    init = init + diff
    diff += 6
    room += 1
