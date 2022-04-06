def convertTime(current: str, correct: str) -> int:
    t1 = int(current.split(":")[0]) * 60 + int(current.split(":")[1])
    t2 = int(correct.split(":")[0]) * 60 + int(correct.split(":")[1])
    temp = abs(t2 - t1)
    cnt1 = temp // 60
    temp = temp % 60
    cnt2 = temp // 15
    temp = temp % 15

    cnt3 = temp // 5
    temp = temp % 5
    cnt4 = temp
    cnt = cnt1 + cnt2 + cnt3 + cnt4
    return cnt

current = "00:00"
correct = "23:59"
res = convertTime(current, correct)
print(res)