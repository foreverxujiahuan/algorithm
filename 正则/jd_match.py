
import re



partten = "https?://item.jd.com/\\d+\\.html?\\?[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"

partten_pc = "https?://dd-static.jd.com[-A-Za-z0-9+&@#/%?=~_|!:,.;]+.(jpg|jpeg|png|bmp)[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"


partten_od = r'(订单号.*交易时间.*\d{2}:\d{2}:\d{2})|(咨询订单号：\d+\s*商品ID：\d+)'

t = re.compile(partten)
t_pc = re.compile(partten_pc)
t_od = re.compile(partten_od, re.DOTALL)

s = "https://item.jd.com/10099244667503.html?sdx=ehi-lLxFuZiE6JnIaIpeiMImtjeUCAgrsmpIsKxAYNqPPe_RLJxf5XjgrErrVGeT"
pc = "https://dd-static.jd.com/ddimg/jfs/t1/208841/8/33091/80184/6618a2cfFe2ec53d8/74eff6fed1d6e58d.jpg"
od = "咨询订单号：29123623929 商品ID：10099423047273"
od2 = "订单号:1316984222317654349\n\n共1件商品,合计￥166.64\n\n交易时间:2020-10-21 02:44:58"

ans = t.match(s)
ans2 = t_pc.match(pc)
ans3 = t_od.match(od)
ans4 = t_od.match(od2)
# print(ans2)
print(ans3)
print(ans4)

