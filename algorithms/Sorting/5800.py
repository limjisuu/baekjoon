class_num = int(input())
for i in range(1, class_num+1):
    data = list(map(int, input().split()))
    student_num, scores = data[0], data[1:]
    scores.sort()
    gaps = [scores[j] - scores[j-1] for j in range(1, student_num)]
    print("Class {i}".format(i=i))
    print("Max {max}, Min {min}, Largest gap {max_gap}".format(max=scores[-1], min=scores[0], max_gap=max(gaps)))
