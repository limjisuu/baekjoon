n = int(input())
files = [input() for _ in range(n)]
pattern = files[0]
answer = ""

for i in range(len(pattern)):
    is_different = False
    for file in files[1:]:
        if file[i] != pattern[i]:
            is_different = True
            break
    if is_different:
        answer += "?"
    else:
        answer += pattern[i]
print(answer)
