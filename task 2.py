def conv():
    b = ''
    while n > 0:
        b = str(n % 4) + b
        n = n // 4

    return b
list = ["в", "и", "н", "т"]

count = conv(1019)[2:]

answer = ''
for i in range(len(count)):
    answer += list[int(count[i])]

print(answer)

