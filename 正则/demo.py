import re
templates = ['我家宝贝<身高> <体重>',
                         '<身高> <体重>',
                         '男生体重<体重>  身高<身高>穿多大呢？',
                         '<体重>/<身高>',
                         '<身高>/<体重>左右s吗？',
                         '女士<身高>身高体重<体重>号码多少',
                         '你好 <身高>/<体重>穿多大码呀',
                         '<体重>体重，<身高>，',
                         '<身高>－<体重>多大',
                         '<体重>－<身高>多大',
                         '<身高>/<体重>穿多大码合适',
                         '<体重>的体重，<身高>的个子',
                         '<体重>重<身高>高',
                         '<身高>/<体重>穿什么码',
                         '<身高>/<体重>穿多大的',
                         '<身高>/<体重>应该m还是l',
                         '<体重>重<身高>高什么码子',
                         '<身高>/<体重>/穿什么号呀',
                         '身高，<身高>体重，<体重>',
                         '<身高>，<体重>',
                         '亲，<身高>-<体重>拍什么号',
                         '<身高>/<体重> 是不是选28',
                         '<身高>/<体重>尺码？',
                         '<身高>,<体重>',
                         '<身高> <体重>穿多大',
                         '<体重>   <身高>',
                         '<身高>.<体重>怎么买？',
                         '<身高>体重不到<体重>',
                         '应该是<身高>/<体重>',
                         '这个我<身高><体重>',
                         '<体重>   <身高>什么码',
                         '这款衣服<体重>体重<身高>身高拍多大',
                         '重<体重>高<身高>',
                         '身高体重<身高>-<体重>',
                         '165的<身高>能穿吗',
                         '170的<身高>能穿吗',
                         '175的<身高>能穿吗',
                         '180的<身高>能穿吗',
                         '185的<身高>能穿吗',
                         '190的<身高>能穿吗',
                         '我家孩子<天龄>了, 穿多大的',
                         '我家孩子<天龄>了',
                         '平时穿<文胸底围>码b穿多大码？'
                         ]

entity_pattern = re.compile("<身高>|<体重>|<年龄>|<文胸底围>")
# for template in templates:
#     matched = entity_pattern.finditer(template)
#     print(template)
#     for match in matched:
#         print(match.group(), match.start(), match.end())

digit_pattern = re.compile("0+")
# s = "000111100011110"
# matched = digit_pattern.finditer(s)
# for match in matched:
#     print(match)


def augment_template(template):
    entity_matches = entity_pattern.finditer(template)
    entity_list = [(match.group(), match.start()) for match in entity_matches]
    digit_list = ['0' for _ in range(len(template))]
    for entity in entity_list:
        for i in range(entity[1], entity[1] + len(entity[0])):
            digit_list[i] = '1'
    digit_str = "".join(digit_list)
    digit_str_matches = digit_pattern.finditer(digit_str)
    digit_list = [(template[match.start(): match.end()], match.start()) for match in digit_str_matches]
    matched_list = digit_list + entity_list
    matched_list.sort(key=lambda t:t[1])
    return matched_list


for template in templates:
    matched_list = augment_template(template)
    print(template)
    print(matched_list)
