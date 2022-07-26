from typing import List


def f(d: dict) -> List:
    for k, v in d.items():
        if v == ['']:
            d[k] = []
    mentions = set()
    for k, values in d.items():
        mentions.add(k)
        mentions.update(set(values))
    n = len(mentions)
    mentions = list(mentions)
    id2mention = dict()
    mention2id = dict()
    for i, mention in enumerate(mentions):
        id2mention[i] = mention
        mention2id[mention] = i
    edges = []
    for k, values in d.items():
        for value in values:
            i, j = mention2id[k], mention2id[value]
            edges.append([i, j])

    g = [[] for _ in range(n)]
    for i, j in edges:
        g[i].append(j)
        g[j].append(i)

    # new
    visited = [False for _ in range(n)]
    ans = []
    cur_set = set()

    def dfs(x: int) -> None:
        nonlocal cur_set
        visited[x] = True
        cur_set.add(x)
        for y in g[x]:
            if not visited[y]:
                dfs(y)

    for i in range(n):
        if not visited[i]:
            cur_set = set()
            dfs(i)
            ans.append(cur_set)
    ans = [{id2mention[i] for i in temp} for temp in ans]
    return ans


def read_json(path):
    return json.load(open(path, 'r', encoding="utf-8"))


if __name__ == '__main__':
    import json

    # path = "/Users/zzulixjh/Desktop/mention2synonyms.json"
    # d = read_json(path)
    # ans = f(d)
    # print(ans)
    print(help(f))