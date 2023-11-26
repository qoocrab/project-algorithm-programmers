# 예상 시간복잡도: O(N)
def solution(record):
    res = []
    uid_dict = {}
    for rec in record:
        uid = rec.split()[1]
        if rec.split()[0] != 'Leave':
            name = rec.split()[2]
            uid_dict[uid] = name
            
    for rec in record:
        action = rec.split()[0]
        uid = rec.split()[1]
        
        if action == 'Enter':
            res.append(f'{uid_dict[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            res.append(f'{uid_dict[uid]}님이 나갔습니다.')
            
    return res
