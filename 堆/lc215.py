def _get_filter_entity(entities):
    sorted_entities = sorted(entities, key=lambda e: (len(e['value']), -e['start']), reverse=True)
    output_entities = []
    output_idexs = set()
    for entity in sorted_entities:
        start, end = entity['start'], entity['end']
        new_set = set(range(start, end))
        if not new_set & output_idexs:
            output_idexs = new_set | output_idexs
            output_entities.append(entity)

    return output_entities


if __name__ == '__main__':
    entity1 = {'start': 0, 'end': 4, 'value': '旺旺3号'}
    entity2 = {'start': 2, 'end': 3, 'value': '3号'}
    entity3 = {'start': 3, 'end': 7, 'value': '旺旺4号'}
    entities = [entity1, entity2, entity3]
    print(_get_filter_entity(entities))
