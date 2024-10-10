import re

# 正则表达式匹配所有中文字符
# pattern = r'[\u4e00-\u9fffA-Za-z0-9。]+'
# pattern = r'[\u4e00-\u9fffA-Za-z0-9\s!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~，。？、；：（）《》【】]'
# pattern = r'[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5A-Za-z0-9,.;:?!]+'
# pattern = re.compile(r'\d\uFE0F\u20E3|\d️⃣')

pattern = r'[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5A-Za-z0-9!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~\s＜✖！️￥×】【～]+'

matcher = re.compile(pattern)

# 测试字符串
s = """合金铰刀  d2.65×25×d3×60l，数量3支，链接发我下"""
# s = "你好hello123大师傅沙发上可以吗？》《.？?收件人: 徐云<>-["
s2 = s + "1️⃣"

# s = "🍎1⃣️"
# s = "你好"

# 使用正则表达式搜索字符串
matches = matcher.fullmatch(s)

if matches:
    print("匹配到的中文字符：", matches)
else:
    print("没有匹配到中文字符。")


matches2 = re.fullmatch(pattern, s2)

if matches:
    print("匹配到的中文字符：", matches2)
else:
    print("没有匹配到中文字符。")

# import random
#
#
# s = [1,2,3]
#
# res = random.choices(s, k=5)
# print(res)







