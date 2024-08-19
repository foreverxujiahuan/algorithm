#
import math

e = math.e
logprobs4text = -0.2319617122411728

ans1 = 0.9499635100364685
ans2 = e ** logprobs4text

print(ans1)
print(ans2)
#
#

# a = [{'detail': {'confidence': 0.8310500383377075, 'match_type': 'UNMATCHED'}, 'intent_name': '消费者询问退货运费如何处理，谁承担，是否需买家垫付', 'matchType': 'UNCERTAIN', 'question': '已经给快递了他那边要运费，我看显示的是无理由退货呗'}]
# print(a)