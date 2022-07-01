# list를 queue처럼 사용하기
q1 = [1,2,3]

q1.append(4) # 맨 뒤에 원소가 추가 됨.
print(q1) # [1, 2, 3, 4]

q1.pop(0) # 맨 앞의 원소가 삭제 됨.
# 그냥 q1.pop()은 맨 뒤의 원소가 삭제되므로 stack구조에서 사용.
print(q1) # [2, 3, 4]


# 역방향 입출력
q2 = [4,5,6]

q2.insert(0,3) # 0위치에 3추가
print(q2) # [3, 4, 5, 6]

q2.pop()
print(q2) # [3, 4, 5]


# 양방향 입출력
from collections import deque

deq = deque([4,5,6])

deq.append(7) # 맨 뒤에 추가
deq.appendleft(3) # 맨 앞에 추가
print(deq)

deq.pop() # 맨 뒤 원소 제거
print(deq)

deq.popleft() # 맨 앞 원소 제거
print(deq)

print(deq[2]) # 인덱스로 값 출력하는것은 리스트와 같다.


# Queue 모듈
from queue import Queue

que = Queue()

que.put(1)
que.put(2)
que.put(3)

print(que) #que의 항목이 출력되지 않음
# print(que[1]) 인덱스로 접근 불가
print(que.get()) # 맨 앞의 1 삭제 및 출력
print(que.get()) # 그 다음 2 삭제 및 출력

print(que.empty()) # 비어있는지 확인