# join
# 문자열을 내림 차순 정렬하는 예제

s = 'adZETsW'
print(s)

#sorted : 정렬 및 리스트로 반환
ss = sorted(s, reverse=True)
print(ss)

# join : 리스트의 원소(문자일때)를 구분자와 함께 결합
sss = ''.join(ss)
print(sss)

n = ['1','3','2'] # 1,3,2 이렇게 숫자를 넣으면
nn = ''.join(n) # join 불가능
print(nn)

arr = [1,2,3]

a = [ (x,x+2) for x in arr]
print(a) # [(1, 3), (2, 4), (3, 5)]

# values = [ x+2 for x in arr ]
print( [ x+2 for x in arr ]) # [3, 4, 5]
