while 1:
    string = input()
    if string == "#":
        break
    if string[-1] == "e":
        last = 0
    else:
        last = 1
    cnt = string.count("1")
    if last % 2 == cnt % 2:
        print(string[:-1] + "0")
    else:
        print(string[:-1] + "1")
