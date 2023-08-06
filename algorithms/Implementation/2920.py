sounds = list(map(int, input().split()))

if sorted(sounds) == sounds:
    print("ascending")
elif sorted(sounds, reverse=True) == sounds:
    print("descending")
else:
    print("mixed")
