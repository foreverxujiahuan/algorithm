import re


# pattern_str = r'(订单号.*交易时间.*\d{2}:\d{2}:\d{2})|(订单:\d+)|(订单号:\d+)|(订单编号:\d+)'
# pattern_str = r'(订单\s*[:|：]\s*(?P<oreder2>\d+))|(订单号\s*[:|：]\s*(?P<oreder3>\d+))|(订单编号\s*[:|：]\s*(?P<oreder4>\d+))'
pattern_str = r'(订单|订单号|订单编号)\s*[:|：]\s*(?P<oreder_id>\d+)'

pattern = re.compile(pattern_str, re.DOTALL)


text1 = "订单号:1316984222317654349\n\n共1件商品,合计￥166.64\n\n交易时间:2020-10-21 02:44:58"
text2 = "订单号 ：1316984222317654349,订单 ：1316984222317654349"
text3 = "dss订单编号:1316984222317654349的撒的撒"
text4 = "订单:1316984222317654349"
text5 = "客服:亲，看到您已拍下，请核对收货地址，我们将尽快为您发出！https://trade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=3900222360313974415_x0003_"
# self.pattern = re.compile(r'(订单号.*交易时间.*\d{2}:\d{2}:\d{2})|(订单:?P<oreder>\d+)|(订单号:?P<order>\d+)|(订单编号:?P<order>\d+)',
#                           re.DOTALL)

# ans1 = pattern.match(text1)
# ans2 = pattern.match(text2)
ans3 = pattern.search(text5)

print(ans3)
print(ans3.groupdict())
print(ans3.group())


