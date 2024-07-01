from typing import List, Tuple


def bisect_search(nums, target_number):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target_number:
            return mid
        if nums[mid] < target_number:
            l = mid + 1
        else:
            r = mid
    return None


def grid_search(M: List[List], N: int) -> List[Tuple[int, int]]:
    ans = []
    r, c = len(M), len(M[0])  # M的size为(m * n)
    for row in range(r):
        col = bisect_search(M[row], N)
        if col is not None:
            ans.append((row, col))
    return ans


if __name__ == '__main__':
    matrix = [[10, 20, 30],
              [11, 21, 45],
              [97, 98, 99]]
    target = 45
    res = grid_search(matrix, target)
    print(res)
