while 1:
    line = input()
    if line == "#":
        break
    alphabet, sentence = line[0], line[2:].lower()
    print(alphabet, sentence.count(alphabet))
