import itertools
import os
import re
import pandas as pd
import sys


control_chars = ''.join(map(chr, itertools.chain(range(0x00, 0x20), range(0x7f, 0xa0))))
control_char_re = re.compile('[%s]' % re.escape(control_chars))


def parse_hex_data(hax_data):
    return bytes.fromhex(hax_data).decode('utf-8')


def remove_control_chars(s):
    return control_char_re.sub(' ', s).strip()


def parse_df_data(df: pd.DataFrame, to_dir):
    buyer_message = df[6]
    buyer_message_time = df[7]
    seller_message = df[9]
    seller_message_time = df[10]
    created_status = df[3] # 1是下单完成，2是协助下单, 4是流失
    chatpeer_id = df[0]

    chatpeer_data = []

    train_data = []
    train_label = []
    new_chatpeer_id = []
    for i in range(len(chatpeer_id)):
        clean_data = []

        if pd.isna(buyer_message[i]):
            print(f"chatpeer_id={chatpeer_id[i]} 没有买家数据，过滤掉！")
            continue
        if pd.isna(seller_message[i]):
            print(f"chatpeer_id={chatpeer_id[i]} 没有客服数据，过滤掉！")
            continue

        _buyer_message = parse_hex_data(buyer_message[i]).split("|$|")
        _buyer_message_time = eval(buyer_message_time[i])
        _seller_message = parse_hex_data(seller_message[i]).split("|$|")
        _seller_message_time = eval(seller_message_time[i])
        if len(_buyer_message_time) != len(_buyer_message):
            print(f"chatpeer_id={chatpeer_id[i]} 买家消息列表长度和买家时间列表长度对不上，过滤掉！")
            print(f"买家消息：{_buyer_message}")
            print(f"买家时间：{_buyer_message_time}")
            continue
        if len(_seller_message_time) != len(_seller_message):
            print(f"chatpeer_id={chatpeer_id[i]} 客服消息列表长度和客服时间列表长度对不上，过滤掉！")
            print(f"买家消息：{_seller_message}")
            print(f"买家时间：{_seller_message_time}")
            continue

        for m, t in zip(_buyer_message, _buyer_message_time):
            clean_data.append((chatpeer_id[i], created_status[i], "买家", remove_control_chars(m), t))

        for m, t in zip(_seller_message, _seller_message_time):
            clean_data.append((chatpeer_id[i], created_status[i], "客服", remove_control_chars(m), t))

        clean_data.sort(key=lambda x: x[-1])
        chatpeer_data.extend(clean_data)

        _x = ""
        for d in clean_data:
            if d[3]:
                _x += f"{d[2]}:{d[3]}|"
        _x = _x[:-1]
        train_data.append(_x)
        train_label.append(created_status[i])
        new_chatpeer_id.append(chatpeer_id[i])

    with open(to_dir, 'w') as f:
        
        for x in train_data:
            f.write(x)
            f.write("\n")

if __name__ == '__main__':
    raw_data_path = sys.argv[1]
    to_dir = sys.argv[2]
    df_data = pd.read_csv(raw_data_path, header=None)
    parse_df_data(df_data, to_dir)