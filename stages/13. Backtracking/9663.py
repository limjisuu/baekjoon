import sys

num = int(sys.stdin.readline())
cnt = 0


def check(sol):
    global cnt
    length = len(sol)

    if length == num:
        cnt += 1
        return

    candidate = list(range(num))
    for i in range(length):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        if sol[i] + length - i in candidate:
            candidate.remove(sol[i] + length - i)
        if sol[i] - length + i in candidate:
            candidate.remove(sol[i] - length + i)

    if candidate:
        for j in candidate:
            sol.append(j)
            check(sol)
            sol.pop()
    else:
        return


for i in range(num):
    check([i])
print(cnt)
