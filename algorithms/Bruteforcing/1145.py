numbers = list(map(int, input().split()))
answer = 10000000000


def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calculate_lcm(a, b, c):
    gcd = calculate_gcd(a, b)
    lcm = a * b // gcd
    gcd = calculate_gcd(lcm, c)
    return lcm * c // gcd


for i in range(4):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            lcm = calculate_lcm(numbers[i], numbers[j], numbers[k])
            if lcm < answer:
                answer = lcm
print(answer)
