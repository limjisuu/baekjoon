import sys
num = int(sys.stdin.readline())
movie_num = 666
cnt = 0
while cnt <= 10000:
    if str(movie_num).count('666') >= 1:
        cnt += 1
    if num == cnt:
        print(movie_num)
        break
    movie_num += 1
