

cur_set = set()
with open("platform.txt", 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line in cur_set:
            print(line)
        cur_set.add(line)
