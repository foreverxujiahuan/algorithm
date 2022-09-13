import re

pattern = re.compile(r'(^|\D)(\+?86)?[ -]?(?P<cell_phone>1\d{2}[ -]?\d{4}[ -]?\d{4})(\D|$)')

text = "15825520793"
matched = pattern.search(text)
ans = matched.span(3)

print(ans)
