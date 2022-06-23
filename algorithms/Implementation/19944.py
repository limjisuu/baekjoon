limit, grade = map(int, input().split())
if grade <= 2:
    print("NEWBIE!")
elif grade <= limit:
    print("OLDBIE!")
else:
    print("TLE!")
