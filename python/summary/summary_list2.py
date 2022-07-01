# 응용편

# stack으로 활용 LIFO
# append() 로 뒤에 넣고 : push 역할
# pop()으로 맨 뒤에 것 제거 : pop
my_stack = [1,2,3]
print(my_stack)

my_stack.append(4)
my_stack.append(5)
print(my_stack)

my_stack.pop()
print(my_stack)


# 혹시 모를 insert 를 방지하기 위해 classify
class MyStack:
    def __init__(self) :
        self.my_list = list()
    
    def push(self, x):
        self.my_list.append(x)

    def pop(self):
        return self.my_list.pop()
    
    def print(self):
        print(self.my_list)


cls_stack = MyStack()
cls_stack.push(3)
print(cls_stack.my_list)
cls_stack.print()


# list 안에 값 포함 여부 확인
print( 3 in my_stack)
print( 3 not in my_stack)

# list comprehension
odd_num = [ x for x in range(1,100) if x%2 == 1]
print(odd_num)


# list 중복 원소 제거 (set 활용)
my_list = [1,3,2,5,6,3,4,1,5,6,7]
my_set = set(my_list) # set은 중복/순서 의 개념이 없음.
my_list = list(my_set)
print(my_list)