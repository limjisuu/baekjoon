string = ""
while True:
    try:
        string += input()
    except EOFError:
        break
answer = sum(map(int, string.split(",")))
print(answer)
