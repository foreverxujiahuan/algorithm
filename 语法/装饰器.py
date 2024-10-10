

recent_message = [{'message_time': '2024-09-09 14:58:10', 'direction': 1, 'content': '就是今天晚上八点是6798？'}, {'message_time': '2024-09-09 14:58:11', 'direction': 1, 'content': '现在拍没有么？'}, {'message_time': '2024-09-09 14:58:12', 'direction': 0, 'content': '亲可以提交订单看下哈'}]
content = "提交了"


def _parse_recent_messages(recent_messages):
    history_content = ""
    for i, msg in enumerate(recent_messages):
        if 'from' not in msg:
            if msg["direction"] == 0:
                history_content += "客服：" + msg['content'] + "\n"
            else:
                history_content += '买家：' + msg['content'] + "\n"
        else:
            history_content += msg['from'] + '：' + msg['content'] + "\n"
    return history_content


def _generate_message_rewrite_prompt(recent_message, content):
    return f"消费者和客服的历史聊天如下：" \
           f"'{_parse_recent_messages(recent_message)}'" \
           f"消费者当前发送的消息为：" \
           f"'{content}'" \
           f"请根据历史聊天记录对当前消费者消息进行改写，输出改写后的文本，要求输出以'消费者：'开头。"


prompt = _generate_message_rewrite_prompt(recent_message, content)
print(prompt)
