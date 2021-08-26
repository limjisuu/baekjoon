word = input()
candidates = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]
        candidate = first[::-1] + second[::-1] + third[::-1]
        candidates.append(candidate)
candidates.sort()
print(candidates[0])
