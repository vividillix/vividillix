str = '\n----------\n'

#list 선언
my_list1 = [1,2,3,4,5]
my_list2 = ['apple', 'banana', 'kiwi', 'lemon']
my_list3 = list() #비어있는 리스트

# for문을 활용한 리스트 선언
L = [i*i for i in range(10)]
print(L)
L = [i for i in L if i % 3 == 0 and i>1]
print(L)
print(str)


# 리스트의 덧셈 곱셈
print(my_list1 + my_list2)
print(my_list1 * 3)
print(str)

# 인덱스
print(my_list2[0])
print(my_list2[-2])
print(str)

print(my_list2.index('apple')) # 값이 해당되는 인덱스 반환
print(my_list2.index('kiwi')) # 값이 해당되는 인덱스 반환
print(str)
 

# 리스트 수정
my_list2[0] = 'grape'
print(my_list2)
print(str)

# 리스트 슬라이싱
print(my_list1[:])
print(my_list1[2:4])
print(my_list1[-5:4])
print(my_list1[::-1]) # offset을 활용한 역순 출력
print(my_list1[3:1]) # 자동 역순 적용 안됨. 빈 리스트 출력
print(my_list1[1:3:-1]) # 역순 적용 안됨. 빈 리스트 출력
print(my_list1[3:1:-1]) # 역순 리스트 출력 list[3] list[2] 원소가 나오게 됨. [1]은 포함 안되니까.
print(str)


# append & insert
my_list1.append(100) # 맨 뒤에 원소 추가.
print(my_list1)
my_list1.insert(0, 99) # 지정한 위치에 원소 추가 
print(my_list1)
print(str)

# 데이터 삭제 
del my_list1[0] # 원하는 인덱스 삭제. 범위에 해당하지 않을 경우 에러
print(my_list1)
del my_list1[1:3]
print(my_list1)

my_list2.remove('lemon') # 원하는 값 처음 1개 삭제. 존재 하지 않을 경우 에러.
print(my_list2)

last = my_list2.pop() # 가장 마지막 원소를 삭제하면서 그 값을 반환
print(last)
print(my_list2)

L.clear() # 모든 원소 삭제. 빈 리스트가 됨.
print('L = ',L)
print(str)

# extend
a = [1,2]
b = [4,5,6]

print(a)
print(a.extend(b)) # 반환값 없음.
print(a) # extend를 하면 a값 자체가 바뀌는 것을 알 수 있음. 사용시 주의!
print(str)

# copy
print(a)
new_a = a.copy()
print(new_a) 
print(id(a))
print(id(new_a))
print(str)

# reverse
print(a)
print(a.reverse()) # 반환값 없음
print(a) # reverse 하면 값 자체가 바뀜.
print(str) 

# sort
# 리스트 요소의 데이터 타입이 같아야함.
print(a)
a.sort() # 값 자체가 바뀜
print("a =",a) 
a.sort(reverse=True) # reverse 값을 True로 하여 내림차순 적용
print("reverse a =",a)  
print(str) 

# 문자는 원래 대문자 -> 소문자 a->z 순으로 정렬 됨.

# count
print(a.count('4')) #0
print(a.count(4)) #1
print(str) 

# deep copy : 독립적인 객체로 복사
my_list4 = [1,2,3]
copy_list = my_list4.copy()
print(my_list4)
print(copy_list)

copy_list[0] = 100
print(my_list4) # 기존 리스트는 바뀌지 않음
print(copy_list) 
print(str) 

# shallow copy : 본체는 동일 객체
copy_list = my_list4
print(my_list4)
print(copy_list)

copy_list[0] = 100
print(my_list4)  # 기존 리스트까지 값 변화가 적용됨.
print(copy_list)

# 2차원 배열 정렬
#time.sort(key=lambda x: (x[1],x[0]))
# 키 설정을 x1 다음 x0 으로 해주겠다ㅡㄴ거임.