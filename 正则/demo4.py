import re

# pattern = re.compile(r'(^|\D)(\+?86)?[ -]?(?P<cell_phone>1\d{2}[ -]?\d{4}[ -]?\d{4})(\D|$)')
#
# text = "15825520793"
# matched = pattern.search(text)
# ans = matched.span(3)
#
# print(ans)

pattern = re.compile(r'你好')

text = "嗷嗷你，啥啥啥好发"
match_terms = pattern.finditer(text)
for match_term in match_terms:
    start, end = match_term.span()
    print(start, end)

# multi_pattern = re.compile(r"BI*")
#
# text = "OOOOOBIOO"
#
# matched = multi_pattern.search(text)
# print(matched.span())