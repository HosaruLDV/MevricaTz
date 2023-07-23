def plus_one(mas):
    complement = 1
    for i in range(len(mas) - 1, -1, -1):
        mas[i] += complement
        complement = mas[i] // 10
        mas[i] %= 10
    if complement > 0:
        mas.insert(0, complement)
    return mas


print(plus_one(mas=[9, 0, 2]))
