import sys
x, y, w, h = map(int, sys.stdin.readline().split())
horizontal = x if x < (w - x) else (w - x)
vertical = y if y < (h - y) else (h - y)
result = horizontal if horizontal < vertical else vertical
print(result)
