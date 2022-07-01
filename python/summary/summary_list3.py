# 리스트는 아니고 리스트 만들때 쓰이는 것 들
# lambda map filter

import math

# map(function, list or tuple)
# list나 tuple에 있는 원소들에 각각 function을 적용한 결과를 반환한다.
# 다시 list() 로 감싸줘야 list 형식으로 사용할 수 있다.

def add_one(n):
    return n+1

my_list1 = [1,2,3,4,5]
print(my_list1)

add_one_list1 = list( map( add_one, my_list1))
print(add_one_list1)
print('---------------\n')

# 람다식
# 함수를 def 형태가 아닌 변수에 저장하는 식
add_one_ramda = lambda x : x+1

my_list2 = [1,2,3,4,5]
print(my_list2)

add_one_list2 = list( map( add_one_ramda, my_list2))
add_one_list2 = list( map( lambda x : x+1 , my_list2)) # 이렇게 변수 처리 안하고 바로 대입도 가능.
print(add_one_list2)
print('---------------\n')

pow2 = lambda x : math.pow(x,2)

my_list3 = [1,2,3,4,5]
print(my_list3)

add_one_list3 = list( map( pow2, my_list3))
print(add_one_list3) # pow의 결과가 실수 형태로 나옴.

add_one_list4 = list( map( math.floor, add_one_list3)) # math의 내장함수를 아예 func위치에 넣을 수도 있음.
print(add_one_list4) 
print('---------------\n')

# filter 
# map과 비슷하지만 map은 반환값을 저장. filter은 반환값이 true이면 원소를 다시 저장.

target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return True if n % 2 == 0 else False # 이 구문도 유용

result = filter(is_even, target) # target에 있는 1이 is_even에 들어가면 결과가 False
# 이때 false가 result에 저장되는게 아니고 1이 저장이 안 되는것, 2는 결과가 true니까 result에 2가 저장됨.

print(list(result))