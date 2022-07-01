import heapq
 
# heap은 최댓값, 최솟값을 찾아내는 연산을 빠르게 하기 위함
# 완전 이진 트리를 기본 형태로 가짐.
# 시간복잡도 log2 N

# heapq 모듈은 최소 힙을 지원하므로, 직접 힙 형태를 구현하지 않아도 됨.

str = '----------\n'
my_heap = list()

# 리스트를 heap으로 바꾸기
heapq.heapify(my_heap)

# insert
heapq.heappush(my_heap,5)
heapq.heappush(my_heap,3)
heapq.heappush(my_heap,7)
print(my_heap) # 3, 5, 7 알아서 오름차순 정렬 됨. 

# delete
heapq.heappop(my_heap) # 가장 앞에 있는 값 (작은 값) 삭제 & 반환
print(my_heap) # 5, 7 알아서 오름차순 정렬 됨. 

# push & pop
heapq.heappushpop(my_heap,30) # push 한 후에 pop & return
print(my_heap) 
print(str)


# 최대 힙 만들기 (내림차순)
# 음수 처리해서 순서 만든 다음, 다시 - 붙여서 리스트 화
my_list = [ 10,1,28,5,14]

reverse_sign = lambda x : x * -1
max_heap = list(map(reverse_sign,my_list)) # 음수 값들로 저장
heapq.heapify(max_heap) # 그 음수로 오름차순 정렬
max_heap = list(map(reverse_sign,max_heap)) # 그 오름차순 된걸 다시 - 처리해서 list로 변경
print(max_heap) # 28 14 10 5 1
print(str)

# 정렬
print(my_list)
print(sorted(my_list)) # sorted는 본체 변경 x
print(my_list)
print(str)

print(my_list)
my_list.sort() # .sort()는 본체 자체를 변경
print(my_list)
print(str)

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # 1 3 7 4 항상 오름 차순으로 나오는게 아님 !!!! 주의 !!!!!
# 그런데 그 스코빌 코테에서 쓸 수 있었던 이유는, 어쨋든 1,2 번째는 제일 작은 값일 거니까 가능했던거 인듯..


if not heap:
    print('이러면 힙의 원소가 없는')
else:
    print('이러면 있는')
