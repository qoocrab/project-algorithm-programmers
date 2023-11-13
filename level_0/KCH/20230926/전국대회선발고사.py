 # 예상 시간복잡도: O(N)
def solution(rank, attendance):
    possible = [ [r, idx] for idx, r in enumerate(rank) if attendance[idx]]
    possible = sorted(possible, key=lambda x: x[0])
    
    return 10000*possible[0][1] + 100*possible[1][1] + possible[2][1]
