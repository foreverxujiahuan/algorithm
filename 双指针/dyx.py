from typing import List


def my_split(text: str):
    symbols = ".，。！？ ~,!?～、…"
    period = "."
    length = len(text)
    output, start_end_list = [], []
    cur_text = ""
    for i in range(length):
        ch = text[i]
        if ch == period and cur_text and cur_text[-1].isdigit() and i+1 < length and text[i+1].isdigit():
            cur_text += ch
        elif ch == period and cur_text:
            output.append(cur_text)
            start_end_list.append((i - len(cur_text), i))
            cur_text = ""
        elif ch not in symbols:
            cur_text += ch
        elif cur_text:
            output.append(cur_text)
            start_end_list.append((i - len(cur_text), i))
            cur_text = ""
    if cur_text:
        output.append(cur_text)
        start_end_list.append((length - len(cur_text), length))
    return output, start_end_list


if __name__ == '__main__':
    text = "aa...d  a，fs3.6，o，d.o34.543.535.rre, up是192.168.100和"
    t1, t2 = my_split(text)
    print(t1)
    print(t2)
