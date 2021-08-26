n = int(input())

for _ in range(n):
    string = input()
    mid = len(string) // 2
    if string[mid-1] == string[mid]:
        print("Do-it")
    else:
        print("Do-it-Not")
