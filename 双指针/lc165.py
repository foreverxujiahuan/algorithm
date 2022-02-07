class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        length = min(len(v1), len(v2))
        flag = 0
        for i in range(length):
            value1 = int(v1[i])
            value2 = int(v2[i])
            if value2 > value1:
                flag = -1
                break
            if value2 < value1:
                flag = 1
                break
        if len(v1) > length and sum([int(v) for v in v1[length:]]) > 0 and flag == 0:
            flag = 1
        if len(v2) > length and sum([int(v) for v in v2[length:]]) > 0 and flag == 0:
            flag = -1
        return flag
