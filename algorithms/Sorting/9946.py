idx = 1
while 1:
    original = input()
    target = input()
    if original == target == "END":
        break
    if sorted(original) == sorted(target):
        print("Case {idx}: same".format(idx=idx))
    else:
        print("Case {idx}: different".format(idx=idx))
    idx += 1
