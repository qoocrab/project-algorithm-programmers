# 예상 시간복잡도: O(N)
def distance(num, l_status, r_status, hand):
    location = {1:[0,0], 2:[0,1], 3:[0,2],
               4:[1,0], 5:[1,1], 6:[1,2],
               7:[2,0], 8:[2,1], 9:[2,2],
               '*':[3,0], 0:[3,1], '#':[3,2]}
    
    dis_l = abs(location[num][0] - location[l_status][0]) + abs(location[num][1] - location[l_status][1])
    dis_r = abs(location[num][0] - location[r_status][0]) + abs(location[num][1] - location[r_status][1])

    if dis_l > dis_r or (dis_l == dis_r and hand[0] == 'r'):
        return 'R', l_status, num
    elif dis_l < dis_r or (dis_l == dis_r and hand[0] == 'l'):
        return 'L', num, r_status

def solution(numbers, hand):
    l_status, r_status = '*', '#'
    res = ''
    
    for num in numbers:
        if num in [1, 4, 7]:
            l_status = num
            res += 'L'
        elif num in [3, 6, 9]:
            r_status = num
            res += 'R'
        else:
            hand_type, l_status, r_status = distance(num, l_status, r_status, hand)
            res += hand_type
            
    return res
