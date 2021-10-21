message = input()
happy = message.count(":-)")
sad = message.count(":-(")

if happy == sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
