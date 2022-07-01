# itertools : 경우의 수 ~!
# 조합 combination

from itertools import combinations, combinations_with_replacement

c = combinations( [1,2,3] , 2 ) # 선택할 원소 리스트 / 선택할 개수
for i in c:
    print(i)
print('-----------------')

cc = combinations_with_replacement( [1,2,3,4] , 2 ) # 중복 허용
for i in cc:
    print(i)

print('-----------------')

# 순열 permutations
from itertools import permutations

p = permutations([1,2,3] , 2) # 리스트 안에서 n개를 순서 고려하여 선택
for i in p:
    print(i)
print('-----------------')

# 카테시안 곱 product
from itertools import product

p = product([1,2,3] , ['a','b']) # 각 리스트에서 하나씩 꺼낼 것임. 이건 순서 없이 나오는거같은데.
for i in p:
    print(i)
print('-----------------')

p = product([1,2,3] , repeat=2) # 한 리스트를 n 번 사용하고 싶을 때. / product를 활용한 중복 순열.
for i in p:
    print(i)


# https://wikidocs.net/21050 assert가 뭔지.. 노 쓸모인듯 ㅎ


# 백준 문제 풀때 빠르게 입력 받기?!

import sys
import math

# sys.stdin.readlines() 로 한번에 입력 다 받기.
# *의 의미는 여러 값들을 콤마로 연결한다- 정도로 받아들이면 될듯.?
trees = [ * map(int, sys.stdin.readlines()[1:])] # 한 줄에 하나의 값 씩 들어오는 상황.
g = math.gcd(*(i - trees[0] for i in trees[1:])) # 그래서 여기서도 ,로 gcd의 인자가 구별되어야하는데 *붙여줌.
print( (trees[-1] - trees[0]) // g + 1 - len(trees) )

## 이건 open으로 받는 법... 
import math
n,*l=map(int,open(0))
l.sort()
l=[w-v for v,w in zip(l,l[1:])]
g=math.gcd(*l)
print(sum(i//g-1 for i in l))
