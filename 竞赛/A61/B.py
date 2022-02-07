from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        length = len(changed)
        if length % 2 == 1:
            return []
        arr1 = [n for n in changed if n % 2 == 1]
        arr2 = [n for n in changed if n % 2 == 0]
        arr2_dict = dict()
        for n in arr2:
            if n not in arr2_dict.keys():
                arr2_dict[n] = 1
            else:
                arr2_dict[n] += 1
        arr3 = []
        for n in arr1:
            if n * 2 in arr2:
                arr3.append(n * 2)
            else:
                return []
        arr3_dict = dict()
        for n in arr3:
            if n not in arr3_dict.keys():
                arr3_dict[n] = 1
            else:
                arr3_dict[n] += 1
        arr4 = []
        for k, v in arr2_dict.items():
            if k not in arr3_dict.keys():
                arr4 += [k] * v
            else:
                arr4 += [k] * (v - arr3_dict[k])
        arr4 = sorted(arr4)
        length2 = len(arr4)
        if length2 % 2 != 0:
            return []
        arr4_dict = dict()
        for n in arr4:
            if n in arr4_dict.keys():
                arr4_dict[n] += 1
            else:
                arr4_dict[n] = 1
        res = []
        if len(arr4_dict.keys()) == 1 and 0 in arr4_dict.keys() and arr4_dict[0] % 2 == 0:
            return [0] * (arr4_dict[0] // 2) + arr1
        for k, v in arr4_dict.items():
            if k == 0:
                res += [0] * (v//2)
                arr4_dict[0] = 0
            elif k * 2 in arr4_dict.keys():
                count = min(arr4_dict[k], arr4_dict[k*2])
                arr4_dict[k * 2] -= v
                res += [k] * count
                arr4_dict[k] -= v
        for k, v in arr4_dict.items():
            if v != 0:
                return []
        res += arr1
        return res


if __name__ == '__main__':
    changed = [0,1,2,0]
    s = Solution()
    res = s.findOriginalArray(changed)
    print(res)
