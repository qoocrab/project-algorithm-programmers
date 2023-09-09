# 예상 시간복잡도: O(n)
def solution(todo_list, finished):
    answer = []
    count = 0
    for i in finished:
        if i is False:
            answer.append(todo_list[count])
        count = count + 1
    return answer