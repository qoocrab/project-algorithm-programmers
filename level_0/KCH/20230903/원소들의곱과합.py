# 예상 시간복잡도: O(N)
def solution(num_list):
    accm_mul, accm_sum = 1, 0
    for i in num_list:
        accm_mul *= i
        accm_sum += i
    
    return 1 if accm_mul < accm_sum**2 else 0

### cf) python 내장함수 eval
