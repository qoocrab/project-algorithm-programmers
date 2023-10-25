# 예상 시간복잡도: O(N)
def solution(lottos, win_nums):
    cnt_to_correct = lottos.count(0)
    corrected_cnt = len(list(set(lottos) & set(win_nums)))
    return [min(7 - corrected_cnt - cnt_to_correct, 6), min(7-corrected_cnt, 6)]
