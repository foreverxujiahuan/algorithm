
import re
entity_pattern = re.compile(r'<.*?>')


def preprocess_template(template):
    term_list = []
    pre_end = 0
    for match in entity_pattern.finditer(template):
        start, end = match.start(), match.end()
        if start != pre_end:
            term_list.append((template[pre_end:start], pre_end))
        term_list.append((template[start:end], start))
        pre_end = end

    if pre_end != len(template):
        term_list.append((template[pre_end:], pre_end))
    return term_list


if __name__ == '__main__':
    template = '<身高><体重> '
    ans = preprocess_template(template)
    print(ans)
