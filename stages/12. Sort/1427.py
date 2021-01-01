import sys
num = sys.stdin.readline()
num_list = []

for i in range(len(num)):
    if num[i] != '\n':
        num_list.append(int(num[i]))
        
num_list.sort(reverse=True)

for i in range(len(num) - 1):
    print(num_list[i], end="")
