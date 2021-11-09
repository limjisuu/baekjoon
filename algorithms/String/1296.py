name = input()
n = int(input())
teams = [input() for _ in range(n)]
percentages = []

for team in teams:
    target = name + team
    l = target.count("L")
    o = target.count("O")
    v = target.count("V")
    e = target.count("E")
    percentages.append((team, ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100))
percentages.sort(key=lambda x: (-x[1], x[0]))
print(percentages[0][0])
