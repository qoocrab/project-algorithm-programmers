# 예상 시간복잡도: O(N)
def solution(my_string):
    return eval(my_string)

#cf) ㄷㄷ 
# def solution(my_string):
    # return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
