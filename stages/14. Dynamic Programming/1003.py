import sys
num = int(sys.stdin.readline())
cnt_zero = [0 for _ in range(41)]
cnt_one = [0 for _ in range(41)]

for n in range(41):
    if n == 0:
        cnt_zero[0] = 1
    elif n == 1:
        cnt_one[1] = 1
    else:
        cnt_zero[n] = cnt_zero[n-1] + cnt_zero[n-2]
        cnt_one[n] = cnt_one[n-1] + cnt_one[n-2]

for i in range(num):
    test_case = int(sys.stdin.readline())
    print(cnt_zero[test_case], cnt_one[test_case])
