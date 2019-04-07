def average_01():
    total = 0.0
    count = 0
    def average(num):
        nonlocal total, count
        total += num
        count += 1
        return total / count
    return average

def average_02():
    total = 0.0
    count = 0
    avg = 0
    while True:
        num = yield avg
        total += num
        count += 1
        avg = total / count

avg_01 = average_01()
print(avg_01(10))
print(avg_01(20))
print(avg_01(30))

avg_02 = average_02()
next(avg_02)
print(avg_02.send(10))
print(avg_02.send(20))
print(avg_02.send(30))