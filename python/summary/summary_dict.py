str = '----------\n'

# 딕셔너리. 순서 없음.
# key는 중복될 수 없고, list와 set이 될 수 없다. (튜플은 가능)
my_dict = {'name':'solji', 'age':'25',('a','b'):'ab', 'hobby' : ['cooking','song']}

# 값 접근
print(my_dict['name']) # key에 숫자가 올 경우 index와 헷갈릴 수 있음.
print(my_dict[('a','b')]) # key에 숫자가 올 경우 index와 헷갈릴 수 있음.
print(my_dict[('a','b')]) # key에 숫자가 올 경우 index와 헷갈릴 수 있음.
print(str)

# 추가 및 변경
my_dict['animal'] = 'dog'
print(my_dict)
my_dict['animal'] = 'cat'
print(my_dict)
print(str)


# 딕셔너리 정렬
my_dict2 = {}
my_dict2[1] = 'fasd'
my_dict2[3] = 'afsd'
my_dict2[4] = 'ssasd'

print(sorted(my_dict2)) # 키 값들만 정렬된 채로 리스트 반환
print(sorted(my_dict2.items())) # 이건 이제 키 기준 정렬되어 밸류까지 반환
print(sorted(my_dict2.items() , reverse=True)) # 반대루 ~

print(sorted(my_dict2.items() ,key = lambda x : x[1])) # 기본적으로 정렬키가 x[0]인데 x[1]로 변경
print(sorted(my_dict2.items() ,key = lambda x : x[1] , reverse=True)) # 기본적으로 정렬키가 x[0]인데 x[1]로 변경


# 같은 밸류가 있다면 ~~~
my_dict2[2] = 'ssasd'
my_dict2[5] = 'ssasd'
print(sorted(my_dict2.items() ,key = lambda x : x[1])) # 4 2 5 순으로 나온다. (아마 입력 기준)
print(sorted(my_dict2.items() ,key = lambda x : (x[1],x[0]))) # 2 4 5 순으로 나온당 ㅎㅎ

# 리스트도 이게 될껄..~~
l = []
l.append( [5,1] )
l.append( [2,5] )
l.append( [3,3] )
l.append( [1,3] )
l.append( [2,3] )

print(sorted(l,key=lambda x:x[1]))
print(l)

# l.sort()
# print(l)
# l.sort(key=lambda x:x[1]) # 이건 알아서 x[0] 값에도 정렬 먹여중
# print(l)
# l.sort(key=lambda x:x[1],reverse=True)
# print(l)