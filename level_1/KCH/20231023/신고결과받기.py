# 예상 시간복잡도: O(N)
def solution(id_list, report, k):
    status = {ID : 0 for ID in id_list} # 누적 신고수
    player = {ID : [] for ID in id_list} # ID를 신고한 사람 명단
    
    for i in set(report):
        normal, abnormal = i.split()
        status[abnormal] += 1
        player[abnormal].append(normal)

    user = {id : 0 for id in id_list} 
    for name in id_list:
        if status[name] >= k:
            for n in player[name]:
                user[n] += 1
            
    return list(user.values())
