# 예상 시간복잡도: O(logN)
def solution(a, b):
    day_list=[31,29,31,30,31,30,31,31,30,31,30,31]
    date_list=['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    return date_list[(sum(day_list[:a-1])+b)%7 -1 ]
