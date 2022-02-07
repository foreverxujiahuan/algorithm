import re
content = '13398985816亚萍150ml'
match = re.findall(r'\d{5,12}|\d{1,4}ml', content)