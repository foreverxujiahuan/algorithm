import random


train_X = []
train_Y = []

for _ in range(10000):
    length = random.randint(5, 100)
    cur_x = ""
    for _ in range(length):
        cur_x += random.choice(["A", "B"])

    train_X.append(cur_x)
    if cur_x.count("A") >= cur_x.count("B"):
        train_Y.append(1)
    else:
        train_Y.append(0)

