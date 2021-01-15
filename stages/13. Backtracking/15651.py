import sys
from itertools import product
n, m = map(int, sys.stdin.readline().split())
product_list = product(range(1, n+1), repeat=m)

for product in product_list:
    for num in product:
        print(num, end=" ")
    print(end="\n")
