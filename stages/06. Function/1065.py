import sys
num = int(sys.stdin.readline())
hansu_list = []
cnt = 0

def hansu(n):
    if 1 <= n <= 99:
        hansu_list.append(n)    # 두 자리 수는 무조건 등차수열을 이룬다
    else:
        ones = int(str(n)[0])
        tens = int(str(n)[1])
        hundreds = int(str(n)[2])
        if tens - ones == hundreds - tens:
            hansu_list.append(n)

for i in range(1, num + 1):
    hansu(i)
    if i in hansu_list:
        cnt += 1
print(cnt)
