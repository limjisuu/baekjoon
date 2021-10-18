while 1:
    try:
        string = input()
        lower, upper, number, space = 0, 0, 0, 0
        for char in string:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                number += 1
            elif char.isspace():
                space += 1
        print(lower, upper, number, space)
    except EOFError:
        break
