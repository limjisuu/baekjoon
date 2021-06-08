import sys
long_name = sys.stdin.readline()
short_name = ""
for char in long_name:
    if char.isupper():
        short_name += char
print(short_name)
