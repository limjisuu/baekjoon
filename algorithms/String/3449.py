n = int(input())

for _ in range(n):
    num1 = input()
    num2 = input()
    result = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            result += 1
    print("Hamming distance is {result}.".format(result=result))
