n, b = map(int, input().split())
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

while n > 0:
    r = n % b
    answer += str(nums[r])
    n //= b

print(answer[::-1])
