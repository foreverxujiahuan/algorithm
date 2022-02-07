def isPalindrome(s: str) -> bool:
    s = s.lower()
    temp = ""
    for t in s:
        if t in "qwertyuiopasdfghjklzxcvbnm1234567890":
            temp += t
    left = 0
    right = len(temp) - 1
    while left < right:
        if temp[left] != temp[right]:
            return False
        left += 1
        right -= 1
    return True


s = ""
res = isPalindrome(s)
print(res)
