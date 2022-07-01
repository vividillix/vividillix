import math

str = '---------------'

print(math.pi)
print(math.e)
print(math.tau)
print(str)

print(abs(-3)) # 절댓값 
print(math.factorial(5)) # 팩토리얼 n * n-1 * ... * 2 * 1
print(str)


# 올림/내림
print(math.ceil(3.2)) # 올림 4
print(math.floor(-3.9)) # 내림 -4 
print(math.trunc(3.7)) # -3 소수점을 그냥 없앰
print(math.trunc(-3.7)) # 3 소수점을 그냥 없앰
print(round(3.2)) #반올림 3
print(round(-3.7)) #반올림 -4
print(str)

# 지수 로그 (결과 : 실수 형태)
print(math.pow(2,10)) # a의b승 
print(math.sqrt(5)) # 4의 제곱근. 음수 대입시 오류
print(math.log(9,3)) # 로그3의 9 = 2
print(math.log10(1000)) # 로그 10의 1000
print(str)


print(math.gcd(18,24)) # 최대공약수
print(math.gcd(18,24,5)) 
print(math.lcm(18,24)) #최소 공배수


# 이거 외에도 각도랑 삼각함수 관련 함수들 있음.

