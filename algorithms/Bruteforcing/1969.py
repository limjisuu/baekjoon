n, m = map(int, input().split())
dna_list = [input() for _ in range(n)]
answer = ""
distance = 0

for i in range(m):
    characters = [dna[i] for dna in dna_list]
    characters.sort()
    char = max(characters, key=characters.count)
    answer += char
    distance += n - characters.count(char)
print(answer)
print(distance)
