

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        list1, list2 = list(s1), list(s2)
        list1[0], list1[2] =  list1[2], list1[0]
        if list1 == list2:
            return True
        list1, list2 = list(s1), list(s2)
        list1[1], list1[3] = list1[3], list1[1]
        if list1 == list2:
            return True
        list1, list2 = list(s1), list(s2)
        list1[1], list1[3] = list1[3], list1[1]
        list1[0], list1[2] =  list1[2], list1[0]
        if list1 == list2:
            return True
        return False