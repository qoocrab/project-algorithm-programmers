# 예상 시간복잡도: O(n)
def solution(num_list):
    answer = num_list
    value = 0
    prev_env_num = num_list[len(num_list)-2]
    env_num = num_list[len(num_list)-1]
    if prev_env_num < env_num:
        value = env_num - prev_env_num
    else:
        value = 2 * env_num
    answer.append(value)
    return answer
