# 예상 시간복잡도: O(m) m : string length
def solution(my_string):
    answer = []
    for i in range(0,len(my_string)):
        if my_string[i].isalpha() is False:
            answer.append(int(my_string[i]))
    answer.sort()
    return answer

print(solution('hi13292'))