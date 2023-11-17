
# def solution(numbers,target):
#     answer=0
#     def a(c_sum,idx):
#         if idx==len(numbers):
#             if target==c_sum:
#                 nonlocal answer
#                 answer+=1
#         else:
#             a(c_sum+numbers[idx],idx+1)
#             a(c_sum-numbers[idx],idx+1)
#     a(0,0)
#     return answer
#
# print(solution([1, 1, 1, 1, 1]	,3))
from collections import deque
def solution(numbers, target):
    answer=0
    q=deque()
    q.append([numbers[0],0])
    q.append([-1*numbers[0],0])
    while q:
        temp, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([temp+numbers[idx], idx])
            q.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
print(solution([1,1,1,1,1],3))