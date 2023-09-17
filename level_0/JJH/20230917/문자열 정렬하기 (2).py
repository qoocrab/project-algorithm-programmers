# 예상 시간복잡도 : O(n)
def solution(my_string):
    answer = [i for i in my_string.lower()]
    answer.sort()

    return ''.join(answer)
