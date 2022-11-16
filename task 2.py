

list = ["в", "и", "н", "т"]

count = str(bin(1019)[2:])

answer = ''
for i in range(len(count)):
    answer += list[int(count[i])]

print(answer)

