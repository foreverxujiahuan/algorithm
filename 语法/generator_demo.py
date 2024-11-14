
def generator(lst):
    for i in lst:
        yield 'a' * i


cur_list = [1, 2, 3, 4]
a = generator(lst=cur_list)
for c in a:
    print(c)

