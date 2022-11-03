from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator2values = dict()
        creator2id_max_value = dict()
        for creator, i, view in zip(creators, ids, views):
            if creator in creator2values.keys():
                creator2values[creator] += view
            else:
                creator2values[creator] = view
            cur = creator2id_max_value.get(creator, ("Z", -1))
            if view > cur[1] or (view == cur[1] and i < cur[0]):
                creator2id_max_value[creator] = (i, view)
        ans = []
        max_value = max(creator2values.values())
        for creator, value in creator2values.items():
            if value == max_value:
                ans.append([creator, creator2id_max_value[creator][0]])
        return ans

if __name__ == '__main__':
    # creators = ["alice", "bob", "alice", "chris"]
    # ids = ["one", "two", "three", "four"]
    # views = [5, 10, 5, 4]
    creators = ["a"]
    ids = ["a"]
    views = [0]
    solution = Solution()
    res = solution.mostPopularCreator(creators, ids, views)
    print(res)


