octal = int(input())
decimal = int(str(octal), 8)
binary = bin(decimal)
print(binary[2:])
