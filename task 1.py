list = ["и", "г", "о", "р", "ь"]


summ = 0
for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    word = f"{list[i1]}{list[i2]}{list[i3]}{list[i4]}{list[i5]}"
                    if word.count('о') == 1 and word.count('ь') == 1 and word[:1] != 'ь':
                        summ+=1

print(summ)

