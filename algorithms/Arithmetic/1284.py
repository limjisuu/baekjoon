while True:
    num = input()
    if num == "0":
        break
    answer = len(num) + 1
    for n in num:
        if n == "0":
            answer += 4
        elif n == "1":
            answer += 2
        else:
            answer += 3
    print(answer)
