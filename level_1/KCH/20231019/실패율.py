# 예상 시간복잡도: O(N)
def solution(N, stages):
    problem_list = [0 for _ in range(N+1)]
    res = []
    for stage in stages:
        problem_list[stage-1] += 1
        
    for i in range(N):
        failure_percent = problem_list[i] / (sum(problem_list[i:]) + 0.0001)
        res.append((-failure_percent, i+1))
   
    return [i for _, i in sorted(res)]
