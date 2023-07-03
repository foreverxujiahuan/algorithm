def extract_entity_positions(tags):
    start_list = []
    length = len(tags)
    for i, tag in enumerate(tags):
        if tag == 1:
            start_list.append(i)
    ans = []
    for start in start_list:
        i = start+1
        end = start + 1
        while i < length and tags[i] == 2:
            end = i+1
            i += 1
        ans.append((start, end))
    return ans


if __name__ == '__main__':
    tags = [0,0,1,0]
    ans = extract_entity_positions(tags)
    print(ans)