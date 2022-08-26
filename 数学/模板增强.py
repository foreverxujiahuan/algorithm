def get_aug_data(entities, template, mentions):
    aug_content = ""
    aug_entities = []
    j = 0
    i = 0
    while i < len(template):
        if j >= len(entities):
            aug_content += template[i:]
            break
        e = '<' + entities[j] + '>'
        length = len(e)
        if template[i: i+length] == e:
            aug_entities.append({
                'entity': entities[j],
                'start': len(aug_content),
                'end': len(aug_content) + len(mentions[j])
            })
            aug_content += mentions[j]
            j += 1
            i += length
        else:
            aug_content += template[i]
            i += 1
    return aug_content, aug_entities


if __name__ == '__main__':
    entities = ('连续实体', '连续实体')
    template = "<连续实体>和<连续实体>有什么区别"
    mentions = ('150v', '80v')
    ans = get_aug_data(entities, template, mentions)
    print(ans)
