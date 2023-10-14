# 예상 시간복잡도: O(N*K), K : 문자열 길이
def solution(babbling):
    cnt = 0
    for bab in babbling:
        if {'_'} == set(bab.replace('aya','_').replace('ye','_').replace('woo','_').replace('ma','_')):
            cnt += 1

    return cnt
