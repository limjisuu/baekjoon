import sys
n = sys.stdin.readline()
for i in range(int(n)):
    num_list = []
    for j in range(len(str(i))):
        x = str(i)[j]
        if x != '\n':
            num_list.append(int(x))
    if i + sum(num_list) == int(n):
        print(i)
        sys.exit(0)
print(0)
