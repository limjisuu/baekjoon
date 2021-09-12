n = int(input())
messages = [input() for _ in range(n)]
for message in messages:
    alphabets = [0 for _ in range(26)]
    answer = "OK"
    i = 0
    while i < len(message):
        alphabets[ord(message[i]) - 65] += 1
        cnt = alphabets[ord(message[i]) - 65]
        if cnt != 0 and cnt % 3 == 0:
            if i == len(message) - 1 or message[i] != message[i+1]:
                answer = "FAKE"
                break
            i += 2
        else:
            i += 1
    print(answer)
