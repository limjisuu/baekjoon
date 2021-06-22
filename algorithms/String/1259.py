num = input()
while num != "0":
    reverse = num[::-1]
    print("yes") if num == reverse else print("no")
    num = input()
