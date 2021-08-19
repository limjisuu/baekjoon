grade = input()
alphabets = {"A": 4, "B": 3, "C": 2, "D": 1}
signs = {"+": 0.3, "0": 0, "-": -0.3}
answer = 0.0 if grade == "F" else alphabets[grade[0]] + signs[grade[1]]
print(float(answer))
