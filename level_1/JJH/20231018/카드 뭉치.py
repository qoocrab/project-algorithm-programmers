def solution(cards1, cards2, goal):
    answer = True
    for i in goal:
        if len(cards1) > 0:
            if i == cards1[0]:
                cards1 = cards1[1:]
                continue

        if len(cards2) > 0:
            if i == cards2[0]:
                cards2 = cards2[1:]
                continue

        answer = False
        break

    if answer:
        return "Yes"
    else:
        return "No"
