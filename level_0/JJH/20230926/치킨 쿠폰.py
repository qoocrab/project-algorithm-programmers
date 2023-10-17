# 예상 시간 복잡도 O(1)
def solution(chicken):
    total_coupon = chicken
    coupon = chicken
    while coupon >= 10:
        remain = coupon % 10
        coupon = coupon // 10
        total_coupon = total_coupon + coupon
        coupon = coupon + remain
    answer = (total_coupon) // 10
    return answer
