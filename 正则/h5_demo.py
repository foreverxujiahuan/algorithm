import re


candidate_texts = [
    "https://h5.m.taobao.com/awp/core/detail.htm?xxc=sendProduct&id=708247402821&ut_sk=1.Zmjn3cjPDfYDAFtCAeWbwe57.21646297.Contacts.cc_chat_share",
    "https://h5.m.taobao.com/awp/core/detail.htm?xxc=sendProduct&id=604296787691&ut_sk=1.ZYWW0s0ayDgDAPd+wmabjyn8.21646297.Contacts.cc_chat_share",
    "https://h5.m.taobao.com/awp/core/detail.htm?xxc=sendProduct&id=695969578581&ut_sk=1.Xtip0x+SQcYDANkKQYjkz8Zy.21646297.Contacts.cc_chat_share"
]

cur_regex = "https?://h5.m.taobao.com/awp/core/detail.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"
regex2 = "https?://h5.m.taobao.com/awp/core/detail.html?\\?.*id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"

match_message = "https://h5.m.taobao.com/awp/core/detail.htm?xxc=sendProduct&id=704526016395&ut_sk=1.Yr45B2Yf9P0DAOEa5wp4wHx9.21646297.Contacts.cc_chat_share"

pattern = re.compile(regex2)

for text in candidate_texts:
    ans = pattern.match(text)
    print(len(text))
    print(ans)


normal_text = ["40的鞋子一次几双嘛", "宁波市华特环境科技有限公司91330212691360290J", "这个没有内存的怎么用"]
intent_names = ["消费者询问商品数量", "消费者询问商品如何选择尺寸", "消费者询问商品是否支持内存卡，支持的内存卡容量、类型"]
samples = ["多少包纸，每包几张？", "白色绿色：", "天语小黄蜂t169最大扩展内存是多少？"]