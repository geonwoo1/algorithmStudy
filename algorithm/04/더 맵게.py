# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해
# Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

import heapq
def solution(a, b):
    cnt=0
    while a[0]<b:
        c=a.pop(0)
        d=a.pop(0)
        a.append(c+2*d)
        a.sort()
        cnt+=1
        if len(a)<=1:
            if a[0]<b:
                cnt=-1
            break
    return cnt

print(solution([1, 2, 3, 9, 10, 12],7))