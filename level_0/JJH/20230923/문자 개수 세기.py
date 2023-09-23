# 예상 시간 복잡도 O(n) n : my_string
def solution(my_string):
    answer = [0 for i in range(0, 52)]
    for i in range(0, len(my_string)):
        char = my_string[i]
        if char.isupper():

            answer[ord(char) - 65] = answer[ord(char) - 65] + 1
        elif char.islower():
            answer[ord(char) - 71] = answer[ord(char) - 71] + 1
    return answer
