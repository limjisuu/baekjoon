string = input()
suffixes = [string[i:] for i in range(len(string))]
suffixes.sort()
for suffix in suffixes:
    print(suffix)
