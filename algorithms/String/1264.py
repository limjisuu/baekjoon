while 1:
    sentence = input().lower()
    if sentence == "#":
        break
    answer = 0
    for char in sentence:
        if char in ["a", "e", "i", "o", "u"]:
            answer += 1
    print(answer)
