

def f(d: dict):
    edges = []
    mentions = set()
    for k, values in d.items():
        mentions.add(k)
        for value in values:
            mentions.add(value)
            edge = [k, value]
            edges.append(edge)
    visited = {k: False for k in mentions}
    cur_set = set()
    ans = []

    def dfs(mention: str) -> None:
        nonlocal cur_set
        visited[mention] = True
        cur_set.add(mention)
        for y in d.get(mention, ''):
            if not visited[y]:
                dfs(y)

    for mention in mentions:
        if not visited[mention]:
            cur_set = set()
            dfs(mention)
            ans.append(cur_set)
    return ans


if __name__ == '__main__':
    d = {'A': ["B"],
         'C': ["B"]}
    res = f(d)
    print(res)
