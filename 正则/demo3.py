import re
import string

text = '的科斯洛夫/:^_^的上课啦'


ans = text.replace('/:^_^', '')
print(ans)
# a = re.compile('/:^_^')
#
# clean_review = a.sub('', text)
# print(clean_review)
