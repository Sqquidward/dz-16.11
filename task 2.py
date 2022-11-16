def conv(n):
    b = ''
    while n > 0:
        b = str(n % 4) + b
        n = n // 4

    return b
list = ["в", "и", "н", "т"]

count = conv(1019)

answer = ''
for i in range(len(count)):
    answer += list[int(count[i])]

print(answer)

