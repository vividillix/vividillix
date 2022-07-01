# 1019
# 책 페이지가 1~N
# 각 숫자가 몇 번 나오는지 구하여라
# 예시) 11 -> 1 4 1 1 1 1 1...
 
 
# 에 바

#######################
# # 1026 보물
# # S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# # 이때 S를 최소화 할 수 있도록 A 재배열

# # B의 가장 큰수와 A의 가장 작은 수가 만나면 되겠다~

# n = int(input())
# # a = input().split()
# # b = input().split()

# # a = [ int(x) for x in a]
# # b = [ int(x) for x in b]

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# # b.sort(reverse=True)

# sum = 0
# # for i in range(n):
# #     sum += int(a[i]) * int(b[i])

# for i in a:
#     t = max(b)
#     sum += i * t
#     b.pop(b.index(t))

# print(sum)
#######################

# 1008 A/B

# num = list(map(int,input().split()))
# num1,num2 = map(int,input().split())
# print(num[0]/num[1])
#######################


# 1010 다리 놓기

# cnt = int(input())
# result = []

# for i in range(cnt):
#     bridge = 1
#     N,M = map(int,input().split())
#     print(N,M)

#     for m in range(M-N+1, M+1):
#         bridge *= m
#     for n in range(2,N+1):
#         bridge //= n
    
#     result.append(bridge)
    
# for r in result:
#     print(r)
    
    
# # 다른 방법
# import sys
# r=sys.stdin.readline

# for _ in range(int(r())):
#     n,m=map(int,r().split())
#     n=min(n,m-n) # 5C2랑 5C3이 똑같아서, n과 m-n중에 작은 수 선택! 시간을 아껴주는 방법.
#     s=1
#     for i in range(n):
#         s=s*(m-i)//(i+1)
#     print(s)
    
    
#######################


# 1021 회전하는 큐

# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# idxs = list(map(int, input().split())) 
# dq = deque([i+1 for i in range(n)])

# cnt = 0

# for idx in idxs:
#     while True:
#         if dq[0] == idx:
#             break
#         else:
#             if dq.index(idx) < len(dq)/2: 
#                 while dq[0] != idx:
#                     dq.append(dq.popleft())
#                     cnt += 1
#             else:
#                 while dq[0] != idx:
#                     dq.appendleft(dq.pop())
#                     cnt += 1
                    
# print(cnt)



# 1018 체스판 다시 칠하기

# n,m = map(int, input().split())
# arr = []
# for i in range(n):
#     arr.append(input())

# # n-7 * m -7 번 반복하면서 최소 값 갱신하기
# # 이때 0이 나오면 바로 0 반환
# cnt = []

# for i in range(n-7):
#     for j in range(m-7):
#         idx1 = 0 # W로 시작하는 경우 바뀌어야하는 수
#         idx2 = 0 # B로 시작하는 경우 바뀌어야하는 수
        
#         for k in range(i,i+8):
#             for r in range(j,j+8):
#                 if (k+r) % 2 == 0: # 짝수면 시작점과 같아야 함.
#                     if arr[k][r] != 'W':
#                         idx1 += 1
#                     if arr[k][r] != 'B':
#                         idx2 += 1
#                 else: # 홀수면 시작점과 달라야 함.
#                     if arr[k][r] != 'B':
#                         idx1 += 1
#                     if arr[k][r] != 'W':
#                         idx2 += 1
                        
#         cnt.append(min(idx1,idx2))

# print(min(cnt))


# 1032 명령 프롬프트
# cnt = int(input())
# words = []
# answer = ''

# for i in range(cnt):
#     words.append(input())
    
# for i in range(len(words[0])):
#     key = ''
#     for w in words:
#         if key == '':
#            key = w[i]
#         else:
#             if(key != w[i]):
#                 answer += '?'
#                 key = ''
#                 break
#     answer += key
    
# print(answer)


# 2839 설탕 배달

# sugar = int(input())
# i = sugar // 5
# # solved = False

# # for k in range(i,-1,-1):
# #     remain = sugar - 5*k
    
# #     if(remain % 3 == 0):
# #         print(k + remain // 3)
# #         solved = True
# #         break
    
# # if(not solved):
# #     print(-1)

# j = sugar % 5
# k = 0

# while i >= 0 :
#     if j % 3 == 0:
#         k = j // 3 
#         break
#     i -= 1
#     j += 5
    
# if j % 3 == 0:
#     print(i +   k)
# else:
#     print(-1)


# 1463 1로 만들기 -- 아직 미완성!

# n = int(input())
# cnt = 0

# while n != 1:
#     if( n%3 == 0):
#         n /= 3
#     elif( n > 8):
#         n -= 1
#     elif( n%2 == 0):
#         n /= 2
#     else:
#         n -= 1
        
#     cnt+=1
    
# print(cnt)


# 1003번 피보나치 함수

# 이렇게 한번에 많은거 처리해야될때는 그냥 싹 다 구해놔!

# 1 반환값 기준으로 저장하기.

# data = [0,1,1]
# result = []
# for i in range(3,41):
#     data.append(data[i-2]+data[i-1])
    
# n = int(input())

# for i in range(n):
#     num = int(input())
#     if(num == 0) :
#         result.append('1 0')
#     else:
#         result.append(str(data[num-1])+' '+str(data[num]))
        
    
# for r in result:
#     print(r)

# 다른 풀이 
# import sys
# T = int(input()) # 입력 받은 수 
# dp = [0,1,1]
# q = [int(sys.stdin.readline()) for _ in range(T)] # 실제 제시 숫자. 이걸 리스트에 저장!

# for i in range(3,max(q)+1): # 시간 단축 위해서 40까지 다 구한게 아니고 최대값 만큼만 구함.
#     dp.append(dp[i-2] + dp[i-1])
    
# for i in q:
#     if(i == 0) :
#         print('1 0')
#     else:
#         print(dp[i-1],dp[i])
        
 
       
# 정수 삼각형

# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
        
        
# # 한 줄 씩 최대값 저장하기
# for i in range(1,n):
#     for j in range(len(arr[i])):
#         # 왼쪽값과 오른쪽값 비교
#         left = 0
#         right = 0
#         if(j>0):
#             left = arr[i-1][j-1]
#         if(j<len(arr[i])-1):
#             right = arr[i-1][j]
            
#         arr[i][j] += max(left,right)

# print(max(arr[-1]))


# 설탕배달

# n = int(input())
# solved = False

# # 3과 5로 구성할 수 있는지 체크
# for i in range(n//5, -1 , -1):
#     remain = n - i * 5
    
#     if(remain%3 == 0):
#         solved = True
#         print(i + remain//3)
#         break;
        
# if not solved:
#     print(-1)



# 1로 만들기

# n = int(input())

# # n 까지의 모든 수의 최소 횟수를 구하기
# d = [0] * (n+1) # 3을 3번째에 넣어주기 위해 하나 더 선언

# for i in range(2,n+1):
    
#     # 일단 이전 + 1 로 횟수 채워주고
#     d[i] = d[i-1] + 1
#     if i % 3 == 0:
#         d[i] = min(d[i],d[i//3]+1)
#     if i % 2 == 0:
#         d[i] = min(d[i],d[i//2]+1)
        
# print(d[n])    


# # 수 찾기
# # 대조군
# n = int(input())
# a = list(map(int,input().split()))
# a.sort()

# # 실험군
# m = int(input())
# b = list(map(int,input().split()))

# # b 안에 있는 애들아 a에 있는지 판별하기
# for i in b:

#     find = False

#     # 이분탐색 조지자는.
#     start = 0
#     end = n-1
    
#     while start <= end:
       
#         mid = (start + end) // 2 

#         mid_val = a[mid]
        
#         if i > mid_val:
#             start = mid + 1
#         elif i < mid_val:
#             end = mid - 1
#         else:
#             find = True
#             break
            
#     if find:
#         print(1)
#     else:
#         print(0)



# 백준 4949 아직 미해결임 ㅡ시 파 ㄹ

# 파이썬은 do while이 없음.

# import re

# arr = []

# # arr에 문자열 입력받기.
# while True:
#     str = input()
#     if str == '.':
#         break
#     else:
#         # 괄호만 추출해서 저장하기
#         arr.append(re.sub(r"[^\(\[\]\)]","",str))


# # yes no를 저장할 배열
# result = []

# # arr의 각 원소에 대해 yes no 판별하기.        
# for s in arr:

#     if s == '':
#         result.append('yes')
#         continue

   
#     paren = []  # 괄호를 저장할 스택 

#     for a in s:
#         if a in ['(', '[']:
#             # 열린 괄호면 그냥 저장.
#             paren.append(a)
            
#         elif a in [')', ']']:
#             # 닫고 싶은데 열린게 없으면 그냥 배열에 넣고 끝냄.
#             if len(paren) == 0:
#                 paren.append(a)
#                 break
    
#             # 열린거 있으면 가장 밖에 있는게 똑같은지 확인
#             last = paren.pop()

#             if a == ')' and last =='(':
#                 continue;
#             elif a == ']' and last =='[':
#                 continue;
#             else:
#                 # 열림 닫힘 매치 안되면 괄호 넣어주고 break
#                 paren.append(a)
#                 break

#     # 문자열 판독 결과 괄호가 남은게 있으면 no                 
#     if len(paren) == 0:
#         result.append('yes')
#     else:
#         result.append('no')
        

# for r in result:
#     print(r)




####### 백준 2798번 블랙잭

# n장의 카드 k 이하
# 각 카드의 숫자 - 정렬 안된 상태임.
# 합이 k에 가장 가까운 3장 고르기

# import itertools

# n, k = map(int,input().split())
# card = map(int,input().split())

# max = 0

# for i in itertools.combinations(card,3):

#     s = sum(i)
#     if s > max and s <= k:
#         max = s
    
# print(max)



#### 백준 2231번 분해합

# 어떤 수 + 각 자리 수 = 제공된 숫자

# def getSum(num):
#     result = 0
    
#     while num > 0:
#         result += num % 10
#         num -= num % 10
#         num /= 10 

#     return int(result)

# n = int(input())

# r = 0
# for i in range(n):
#     if getSum(i) + i == n:
#         r = 1
#         print(i)
        
#         break;
    
# if r == 0:     
#     print(0)    



### 백준 1929번 소수 구하기 시간 초과 뜸
# 이거 누구꺼 보니까 n 의 제곱 ~ n+1의 제곱 사이의 수에 대해서
# n으로 나눠지는지를 판단하던데..

# def isPrime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# # M 이상 N 이하의 모든 소수 출력
# m,n = map(int,input().split())

# for i in range(m,n+1):
#     if isPrime(i):
#         print(i)



### 백준 11659번 구간 합 구하기 -  왜 시간 초 ㅡㅡ???? 다 더한담에 빼는 식으로 해볼까.. 이게 맞넹.

# # 숫자 n개, 구간 m개
# n,m = map(int,input().split())

# # 숫자 목록
# nums = list(map(int,input().split()))
# sum = sum(nums)
# sums = []

# # 각 위치까지의 총 합 구하기
# for i in range(1,n+1):
#     sums.append(sum)
#     sum -= nums[n-i]
# sums.append(0)
# sums.reverse()

# print(sums)

# result = []
# for i in range(m):
#     a,b = map(int,input().split())

#     result.append(sums[b] - sums[a-1])
    
# for r in result:
#     print(r)



#### 백준 9663번 N-Queen 백트래킹 연습 예제

# # 퀸이 놓여지면 대각선, 직선에 뭐 못둠. 즉 가로 한줄에 하나

# # n * n 체스판
# n = int(input())

# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         # 윗줄에 놓인 열이랑 똑같으면 직선, k번째 윗줄에 있는거랑 k만큼 차이나면 대각선이라 안됨.
#         if row[x] == row[i] or abs(x-i) == abs(row[x] - row[i]):
#             return False
        
#     return True

# def n_queens(x):
#     print(x, '번째 행 시작.')
#     global ans # 이건 머냥. 이 함수에서 공통으로 쓰는 애야?
    
#     if x == n:
#         ans += 1 # 마지막 까지 잘 실행이 됐다는 뜻이니까 정답 개수 하나 올려줌
#         return
#     else:
#         for i in range(n): 
#             row[x] = i
#             if is_promising(x):
#                 print(i,' 에다가 놓고,' ,x,' 다음꺼 불러봐')
#                 n_queens(x+1)
                
                
# n_queens(0)
# print(ans)




#### 백준 15649번

# n, m = map(int,input().split())
# ans = [0] * m


# # 1부터 n까지 자연수 중에 중복없이 m개를 고른 수열을 모두 구하여라.
# # 각 수열은 공백으로 구분
# # 사전 순으로 증가.

# # x 번째 원소가 그 앞에 나온거랑 중복 안되는 지.
# def is_promising(x):
#     for i in range(x):
#         if ans[i] == ans[x]:
#             return False
        
#     return True

# def sol(x):
#     if x == m:
#         print(' '.join(ans))
#         return
#     else:
#         for i in range(n): 
#             ans[x] = str(i+1)
#             if is_promising(x):
#                 sol(x+1)
                
# sol(0)

### 15650번

# n, m = map(int,input().split())
# ans = [0] * (m+1)
 
# def sol(x):
#     if x == m+1:
#         result = list(map(str,ans))[1:]
#         print(' '.join(result))
#         return
#     else:
#         for i in range(ans[x-1]+1,n+1):
#             ans[x] = i
#             sol(x+1)
                
# sol(1)




#### 백준 14888번

# n = int(input()) # 사용할 숫자 개수
# nums = list(map(int,input().split())) # 숫자 목록 순서 그대로!
# oper = list(map(int,input().split())) # + - x % 개수

# min = 2e9
# max = 2e9 * -1


# # x 번째에 연산자를 할당하는 함수. , r은 이전까지 결과값.
# def calcul(x,result):
    
#     print(x,'번째 연산자',result)
    
#     global min
#     global max
    
#     # 이미 다 채웠으면..
#     if x == n-1:
#         print('결과는 = ',result)
#         print()
#         if result > max:
#             max = result
#         if result < min:
#             min = result
#         return
    
#     temp = result
    
#     # 더하기    
#     if oper[0] != 0:
#         print('더하기')
#         result += nums[x+1]
#         oper[0] -= 1
        
#         calcul(x+1, result)
#         oper[0] += 1
#         result = temp
        
#     # 빼기    
#     if oper[1] != 0:
#         print('빼기')
#         result -= nums[x+1]
#         oper[1] -= 1
        
#         calcul(x+1, result)
#         oper[1] += 1
#         result = temp
        
#     # 곱하귀    
#     if oper[2] != 0:
#         print('곱하기')
#         result *= nums[x+1]
#         oper[2] -= 1
        
#         calcul(x+1, result)
#         oper[2] += 1
#         result = temp
        
#     # 나눅이    
#     if oper[3] != 0:
#         print('나누기')
#         if result < 0 :
#             result = abs(result)// nums[x+1] * -1
#         else:
#             result //= nums[x+1]
            
#         oper[3] -= 1
#         calcul(x+1, result)
#         oper[3] += 1
#         result = temp

# calcul(0,nums[0])

# print(max)
# print(min)



#### 백준 14889번

# # 정보 초기화
# n = int(input())
# ability = []
# for i in range(n):
#     temp = list(map(int,input().split()))
#     ability.append(temp)
    
# # 첫번째 팀을 중복없이 n/2 명 뽑기.
# global team_a
# team_a = [0] * ( n //2  + 1)
# min = 2e9

# def cal():
#     global min
    
#     # 두번째 팀 구성하기
#     team_b = [ x for x in range(1,n+1) if x not in team_a[1:]] 
    
#     # 각 팀의 능력치 합.
#     tot_a = 0
#     tot_b = 0

#     for i in team_a[1:]:
#         for j in team_a[1:]:
#             tot_a += ability[i-1][j-1]

#     # 두번째 팀 능력치 합.
#     for i in team_b:
#         for j in team_b:
#             tot_b += ability[i-1][j-1]

#     temp = abs(tot_b - tot_a)
    
#     if min > temp:
#         min = temp
        
#     return 

# # x번째 인덱스에 사람 배정하기.
# def sol(x):
#     # 사람 다 채웠으면 능력치 차이 계산해.
#     if x == n//2 + 1:
#         cal()
#         return
    
#     # 이미 들어간 값보다 큰 값만 새로 넣기. -> 그래서 중복 비교할 필요가 없지? 어짜피 각 사람당 숫자가 다 다르니까!
#     for i in range(team_a[x-1], n):
#         team_a[x] = i + 1
#         sol(x+1)    
    
# sol(1)
# print(min)



#### 백준 1991번 트리 순회

# n = int(input())
# tree = []
# for i in range(n):
#     tree.append(input().split())
    
    
# # 전위 순회
# def front(x):
#     print(x[0],end='')
    
#     if x[1] != '.':
#         for t in tree:
#             if t[0] == x[1]:
#                 front(t)
    
#     if x[2] != '.':
#         for t in tree:
#             if t[0] == x[2]:
#                 front(t)

# # 중위 순회
# def middle(x):
    
#     if x[1] != '.':
#         for t in tree:
#             if t[0] == x[1]:
#                 middle(t)
    
#     print(x[0],end='')
    
#     if x[2] != '.':
#         for t in tree:
#             if t[0] == x[2]:
#                 middle(t)

# # 후위 순회
# def back(x):
#     if x[1] != '.':
#         for t in tree:
#             if t[0] == x[1]:
#                 back(t)
    
#     if x[2] != '.':
#         for t in tree:
#             if t[0] == x[2]:
#                 back(t)
                
#     print(x[0],end='')

# front(tree[0])
# print()
# middle(tree[0])
# print()
# back(tree[0])


### 백준 11725번 트리 부모 찾기 ------------------------ 미해결 ㅜㅜㅜ

# 루트는 1

# n = int(input())
# pair = []

# for i in range(n-1):
#     pair.append(list(map(int,input().split())))
    

# parent = [0] * (n+1) # 인덱스 + 1의 부모값을 저장할거임. 아직 없으면 -1 상태 
# parent[1] = 1
    
# idx = 0
# while pair:
#     if idx >= len(pair):
#         idx = 0
    
#     p = pair[idx]
    
#     # p의 두개의 값 중에. 부모가 있는 애의 값을 없는 애의 인뎃ㄱ스에 넣어줌.
#     if parent[p[0]] != 0: #이놈 부모가 있어 
#         parent[p[1]] = p[0]
#         pair.remove(p)
#     elif parent[p[1]] != 0:
#         parent[p[0]] = p[1]
#         pair.remove(p)
#     else:
#         # 만약 둘다 이미 나온게 없다면 ???
#         # 그냥 idx만 증가.
#         idx += 1
        
# for p in parent[2:]:
#     print(p)


### 백준 1992번 쿼드 트리 --------------------- 미해결 아래  코드 해석하기..

# 주어진 배열 4등분해서 0 , 1 로 구분

# n = int(input())

# tree = [list(map(int,(input()))) for _ in range(n)]
# print(tree)
# result = []

# def quad_tree(x,y,n):
#     global result
#     color = tree[x][y]

#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != tree[i][j]: # 범위안에 한개라도 다른경우는 4분면으로 나눠서 다시 검색
#                 result.append("(") # 4분면으로 나눌때 괄호를 친다.
#                 quad_tree(x,y,n//2)
#                 quad_tree(x, y+n//2, n//2)
#                 quad_tree(x+n//2, y, n//2)
#                 quad_tree(x+n//2, y+n//2, n//2)
#                 result.append(")")
#                 return
#     result.append(color) # 재귀로 안들어가고 for문이 전부 다 끝난 상태이기 때문에 범위안에 모든수가 같다고 볼 수 있다.

# quad_tree(0,0,n)
# print("".join(map(str,(result))))



#### 백준 10815번 숫자 카드

# # 갖고 있는 카드
# n = int(input())
# nums = list(map(int,input().split()))
# nums.sort()

# # 나에게 있는지 판별할 카드
# m = int(input())
# test = list(map(int,input().split()))

# result = []

# for t in test:
#     # 이제 t가 있는지 없는지 이 분 탐 색 -!
#     find = False
    
#     start = 0
#     end = len(nums) - 1
    
#     while start <= end:
        
#         mid = ( start + end ) // 2
        
#         if nums[mid] < t:
#             start = mid + 1
#         elif nums[mid] > t:
#             end = mid - 1
#         else:
#             result.append('1')
#             find = True    
#             break
    
#     if not find:
#         result.append('0')
        
        
# print(' '.join(result))



#### 백준 10816번 숫자 카드 2 + 개수까지 출력을 해주어야 한다.!
## https://chancoding.tistory.com/45
 
# # 그냥 매번 count()해버리면 시간 초과 뜸.

# # 갖고 있는 카드 (기존 값)

# n = int(input())
# nums = list(map(int,input().split()))

# # 나에게 있는지 판별할 카드
# m = int(input())
# test = list(map(int,input().split()))

# # 중복 제거 & 정렬
# set_nums = list(set(nums))
# set_nums.sort()

# # 값 : 개수 저장
# num_cnt = {}
# for i in set_nums:
#     num_cnt[i] = str(nums.count(i))

# result = []

# for t in test:
#     # 이제 t가 있는지 없는지 이 분 탐 색 -!
#     find = False
    
#     start = 0
#     end = len(set_nums) - 1
    
#     while start <= end:
        
#         mid = ( start + end ) // 2
#         target = set_nums[mid]
        
#         if target < t:
#             start = mid + 1
#         elif target > t:
#             end = mid - 1
#         else:
#             result.append(num_cnt[target])
#             find = True    
#             break
    
#     if not find:
#         result.append('0')
        
        
# print(' '.join(result))




# ### 10828 스택

# n = int(input())

# my_stack = []
# result = []

# for i in range(n):
#     t = input()
    
#     if t == 'top':
#         result.append(my_stack[-1] if my_stack else -1)
        
#     elif t == 'pop':
#         result.append(my_stack.pop() if my_stack else -1)
        
#     elif t == 'size':
#         result.append(len(my_stack))
    
#     elif t == 'empty':
#         result.append(0 if my_stack else 1)
    
#     else:
#         n = t.split()[1]
#         my_stack.append(int(n))
        
    
# for r in result:
#     print(r)
     
    

# ### 1406 에디터 -- 지금 할 기분이 아니여 ㅡㅡ
#    https://seongonion.tistory.com/53
# s = input() 
# n = int(input())

# my_stack = list(s)
# idx = len(s) + 1
# max_idx = idx

# for i in range(n):
#     t = input()
    
#     if t == 'L':
#         if idx > 1:
#             idx -= 1 
        
#     elif t == 'D':
#         if idx < max_idx:
#             idx += 1 
        
#     elif t == 'B':
#         if idx > 1:
#             my_stack.pop(idx-2)
#             max_idx -= 1
#             idx -= 1
    
#     else:
#         n = t.split()[1]
#         my_stack.insert(idx-1,n)
#         idx += 1
#         max_idx += 1
        
# print(''.join(my_stack))
        

#### 17298번 --- 인덱스를 스택에 저장하기 ... 

# n = int(input())
# nums = list(map(int,input().split()))

# result = []
# for i in range(n):
#     a = nums[i]
#     for j in range(i+1,n):
#         if a < nums[j]:
#             result.append(str(nums[j]))
#             break
#         if j == n-1:
#             result.append(str(-1))
            
# result.append(str(-1))

# print(' '.join(result))



### 11729 하노이 이동 [재귀] - 한번에 맞췄따 ㅜㅜㅜㅜㅜㅜ

# 항상 위 < 아래 
# 옮긴 횟수와 어디서 어디로 옮기는 지 출력.

# def hanoi(t, now, next):
#     # t개를 now 에서 next로 이동 시킬거임.
#     # 그럼 t-1개를 제 3의 지역으로 보내면 됨.
    
#     if t > 1:
#         hanoi(t-1,now,6-now-next)
#         print(now, next)
#         hanoi(t-1,6-now-next,next)
        
#     else:
#         print(now, next)
        

# n = int(input())

# # 총 횟수만 따로 구하기
# cnt = [1]
# for i in range(1,n):
#     cnt.append(cnt[i-1] * 2 + 1)

# print(cnt[-1])
# hanoi(n,1,3)



### 5568 카드 놓기 [재귀] 이게 재귀야 ??? 그냥 순열로 푸는법
# 아 재귀로 그냥 쌩으로 순열을 만들으라는 거였음..

# n장 내려놓기 / 카드는 1~99 중복 가능
# k장 선택하기  / 가로로 정수 만들기

# from itertools import permutations

# n = int(input())
# k = int(input())

# cards = [input() for _ in range(n)]
# res = set()    

# for per in permutations(cards,k) :
#     res.add(''.join(per))
    
# print(len(res))


### 6603 

# from itertools import combinations

# result = []

# while True:
#     k = input()
    
#     if k != '0':
#         s = k.split()[1:]
        
#         for p in combinations(s,6):
#             result.append(' '.join(list(p)))
#         result.append('')

#     else:
#         break

# result.pop()
# for r in result:
#     print(r)



# ### 11399 ATM 그리디 알고리즘

# # n 명의 사람. i번째 사람은 P[i] 의 시간이 걸림
# # 최소 대기시간을 구하고 싶대.

# n = int(input())
# p = list(map(int,input().split()))
# p.sort()

# for i in range(n-1):
#     p[i+1] += p[i]

# print(sum(p))


### 11047 동전 0 그리디

# # n종류의 동전으로 
# # k만큼 만드는 최소 개수
# # 동전은 항상 이전것의 배수임. -> 이 조건이 그리디를 가능하게 함.

# n,k = map(int,input().split())

# coin = [int(input()) for _ in range(n)]
# coin.reverse()

# t = 0
# for c in coin:
#     m = k // c
#     k -= m * c
#     t += m
    
# print(t)




# ### 1931 회의실 배정 !! 다시 한번 해보기!

# # 회의실 하나 N개의 회의
# # 회의가 겹치지않게 가장 많은 회의 수
# # 시작시간 , 종료시간 - 종료시간 기준으로 정렬된다면
# #  +++ 종료 시간 다음으로 시작시간도 정렬을 해줘야 바로 끝나는 걸 처리 해줄 수 있음
# # 2 2 / 1 2 같은경우 2 2 부터 해버리면 1 2 를 못하는데
# #  1 2 부터 하면 2 2 도 할 수 있거든.

# n = int(input())
# time = [ list(map(int,input().split())) for _ in range(n)]
# time.sort(key=lambda x: (x[1],x[0]))

# print(time)

# end = 0
# cnt = 0
# for t in time:
#     # 시작시간이 끝나는 시간보다 나중이면
#     if t[0] >= end:
#         end = t[1]
#         cnt += 1
#         print(t)

# print(cnt)



# #### 2217 로프 디그리!

# # k개의 로프를 사용하여 w인 물체를 들어올리면 균등분배
# # 들어올릴 수 있는 최대 무게!

# n = int(input())
# rope = [int(input()) for _ in range(n)]
# rope.sort()

# max = 0
# for i in range(n):

#     if max < rope[i] * (n-i) :
#         max = rope[i] * (n-i)

# print(max)


# ### 10162

# # 버튼 3개 300초 60초 10초
# # 정확히 T초를 맞춰야 함. 버튼 누르는걸 최소로.
# # 설정 불가능하면 -1

# t = int(input())
# btn = [300,60,10]

# res = []
# if t % 10 != 0 :
#     print(-1)
# else:
#     for b in btn:    
#         cnt = t // b
#         t -= b * cnt
#         res.append(str(cnt))
        
#     print(' '.join(res))



# #### 13305 주유소

# # n개의 도시 왼->오 이동
# # 주유소당 가격이 다름 최소 기름값

# n = int(input())
# dis = list(map(int,input().split()))
# cost = list(map(int,input().split()))

# result = 0
# pre = cost[0]

# for i in range(n-1):
#     if cost[i] < pre:
#         pre = cost[i]
#     result += dis[i] * pre

# print(result)


# #### 2309 일곱 난쟁이 -브루트 포스 (완탐)

# h = [int(input()) for _ in range(9)]
# h.sort()

# # 9개의 값 중에 2개 빼고 100이 되어야 함
# # 투포인터로 해보고싶은걸 ! 성공
 
# extra = sum(h) - 100 # 초과한 키

# left = 0
# right = 8

# while left < right:
#     t = h[left] + h[right]
#     if t == extra:
#         h.pop(left)
#         h.pop(right - 1)
#         break
#     elif t > extra:
#         right -= 1
#     else:
#         left += 1
        

# for hh in h:
#     print(hh)



### 2661 좋은 수열 / 백트래킹 --------- 다시 해라잉..

# 123으로 이루어진 수열, 인접한 동일 수열이 없어야됨.
# N자리의 자리수 중에서 가장 작은 좋은 수열

# def isGood(n):
#     print('지금 판별할 숫자',n)
    
#     # i는 비교할 글자 단위
#     for i in range(1,len(n)//2+1):
#         print(i,'개씩 판별할 예정')
        
#         left = 0 # 시작인덱스
#         right = i
        
#         while right + i < len(n) + 1:
#             print(left, right)
#             print(n[left:left + 1] , n[right:right + 1])
            
#             if n[left:left + i] == n[right:right + i]:
#                 return False
            
#             left += 1
#             right += 1
    
#     return True

# from itertools import product

# n = int(input())

# # print(isGood([1,2,1,3,1,2,1]))


# for i in product(range(1,4),repeat=n):
#     if isGood(list(i)):
#         print(i)
#         break
    
    

# ++ 처음부터 7자리 다 보는게 아니고.. 앞에서부터 하나씩 추가해보기?
# 백트래킹이래잔어....... 그럼 시바 머 어째야대


# # 전달받은 원소들이 유효한지 확인하는 함수
# def isGood(arr,cnt):
    
#     # k는 즉 시작점을 의미.
#     for k in range(cnt):
#         tmp = arr[k:] 
        
#         # i는 비교할 간격을 의미
#         for i in range(1, len(tmp) // 2 + 1):
#             checkV = tmp[:i]
#             if checkV == tmp[i:i+i]:
#                 return False

#     return True

# # 원소 결정하는 함수
# def backTracking(count):
    
#     if not isGood(arr,count):
#         return -1
    
#     if count == n:
#         print(arr)
#         return 0
    
#     for i in range(1,4):
#         arr.append(i)
#         if backTracking(count + 1) == 0:
#             return 0
#         arr.pop()


# n = int(input())
# arr = []
# backTracking(0)



# ### 2667 ----------- 코드 정리만 다시 해보기ㅣㅣㅣㅣ

# # 인자로 받은거 상하좌우 확인하고 집이면 단지 번호로 바꿔줌 --- 코드 줄여보기.. 정리좀....ㅋ...
# # 그리고 지금 이건 cnt가 1 2 3 으로 안되고 끊길때마다 1씩 증가돼서.. 이것도 해결할 수 있으면 해보기.
# def check(i,j):
#     global tot
    
#     if map[i][j] == '0': # 집이 아니면 ..
#         visit[i][j] = -1
#         return
    
#     else: # 집이면
        
#         if visit[i][j] != 0:
#             return
    
#         visit[i][j] = cnt
#         tot += 1
          
#         # 상
#         if i > 0:
#             check(i-1,j)
#         # 하
#         if i < n-1:
#             check(i+1,j)
#         # 좌
#         if j > 0:
#             check(i,j-1)
#         # 우
#         if j < n-1:
#             check(i,j+1)
            

# n = int(input())
# cnt = 1

# visit = []
# map = []

# global tot
# tot = 0
# home = []


# for _ in range(n):
#     map.append(input())
#     visit.append([0]*n)
    
# for i in range(n):
#     for j in range(n):
#         if visit[i][j] == 0:
#             check(i,j)
            
#             if tot != 0:
#                 home.append(tot)
#             cnt += 1
#             tot = 0 
 
# print(len(home))
# home.sort()

# for h in home:
#     print(h)




### 2485번 -- 아래에 짧은 버전.... 어디서 속도 차이가 나는거지

# import math

# n = int(input())
# trees = [ int(input()) for _ in range(n)]

# dis = []
# for i in range(1,n):
#     dis.append(trees[i] - trees[i-1])

# g = math.gcd(dis[0],dis[1])
# for i in range(1,n-1):
#     g = math.gcd(g,dis[i])

# cnt = 0
# for d in dis:
#     cnt += d // g -1

# print(cnt)

# import math

# # n,*trees = map(int,open(0)) # 여러 입력 한번에 받을때 open(0)...
# # 0은 stdin, 1은 stdout, 2는 stderr에 각각 해당해서 그렇습니다.
# n = int(input())
# trees = [ int(input()) for _ in range(n)]

# assert n == len(trees) , 'zz' #이건 그냥 확인문.. 

# trees.sort()
# # trees = [ ] # 거리 구할 때 계속 인덱스로 접근하는거보다 zip처리 해주기.?

# dis = []
# for i in range(1,n):
#     dis.append(trees[i] - trees[i-1])

# g = math.gcd(*trees) # 이렇게 포인터 처리 해주면 여러값 콤마로 인자 전달 가능 ㄷ 

# cnt = 0
# for d in dis:
#     cnt += d // g -1

# print(cnt)


# import math
# n,*l=map(int,open(0))
# assert n==len(l)
# l.sort()
# l=[w-v for v,w in zip(l,l[1:])]
# g=math.gcd(*l)
# print(sum(i//g-1 for i in l))

# import sys
# import math

# trees = [ * map(int, sys.stdin.readlines()[1:])] # 이거는 그 머냐... open이랑 얘는 터미널에서는 테스트 할수가 없음.. 일단 다른 코드로 받은 다음에 

# g = math.gcd(*(i - trees[0] for i in trees[1:]))

# print( (trees[-1] - trees[0]) // g + 1 - len(trees) )


### 2606 바이러스

# 1번이랑 연결된 모든 애.. 구해라..
from collections import deque

n = int(input()) # 컴퓨터 수
m = int(input()) # 연결 수

com = [ [0] * n for _ in range(n)]

# 컴퓨터 연결 된 쌍에 1 체크
for _ in range(m):
    a,b = map(int,input().split())
    com[a-1][b-1] = 1
    com[b-1][a-1] = 1
    
# 1부터 큐에다가 연결된 거 추가
virus = deque([0])
visit = [0] * n

cnt = 0

while virus:
    idx = virus.popleft()
    
    for k in range(n):
        if com[idx][k] == 1:
            if visit[k] == 0:
                visit[k] = 1
                virus.append(k)
                cnt += 1
        
print(cnt-1)