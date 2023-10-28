# 예상 시간 복잡도 O(n^2) n is length of numbers
def solution(numbers):
    answer = []
    for i in range(0,len(numbers)):
        for k in range(i+1,len(numbers)):
            if numbers[i] + numbers[k] in answer:
                pass
            else:
                answer.append(numbers[i] + numbers[k])
    answer.sort()
    return answer
