import re

text = "这个<家电-品类>可以和<3C数码-手机型号>适配吗"

# s = "1234feges24"

pattern = "<([\w-]+)>"
# pattern2 = "(?P<digit>\d+?)"

#


s = "1234feges24"
# pattern = "(?P<digit>\d+?)"
t = re.compile(pattern)
matched = t.match(s)
# print(matched.groupdict())
ans = t.findall(text)
print(ans)
