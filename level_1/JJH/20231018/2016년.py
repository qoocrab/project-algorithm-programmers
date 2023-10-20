def solution(a, b):
    dayList = ["THU", "FRI","SAT","SUN","MON","TUE","WED"]
    day = 0
    for i in range(1,a):
        if i < 8:
            if i % 2 == 0:
                if i == 2:
                    day = day + 29
                else:
                    day = day + 30
            else:
                day = day + 31
        else:
            if i % 2 == 0:
                day = day + 31
            else:
                day = day + 30
    day = day + b
    answer = dayList[day%7]
    return answer
