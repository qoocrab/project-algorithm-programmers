# 예상 시간복잡도: O(N)
def solution(todo_list, finished):
    return [todo for todo, finish_flag in zip(todo_list, finished) if not finish_flag ]
