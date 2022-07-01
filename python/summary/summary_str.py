str = '\n----------\n'
str1 = 'I like fruits'

#Plus. 내장함수 사용 후 기존 변수의 값이 바뀌는지 항상 유념하기.

# 문자열의 길이 
print(len(str1))
print(str)
# str1[0] = 'F' 오류 발생.
# 문자열은 수정할 수 없다.
# str1 = 'dd' 아예 새로 할당은 물론 가능.

 
# 따옴표 3개를 사용하여 개행이 포함된 문자열 선언
str2 = '''나는
솔지다
알겠냐.'''
print(str2) 
print(len(str2)) #11
print(str)

# 문자열 내부에 기호 표현하기 \ + 원하는 기호
str3 = '역슬래시 \\  개행 \n탭 \t 작은 따옴표 \' '
print(str3)
print(str)


#문자열 인덱싱과 슬라이싱
print(str1)
print(str1[0])
print(str1[-2])
print(str1[2:5])
print(str1[:]) # 공백은 저절로 맨앞과 맨뒤 지정
print(str1[::-1]) #역방향으로 출력 stiurf ekil I
print(str1[::2]) #2칸씩 건너뛰어 출력
print(str)

#count
print(str1)
print(str1.count('i')) # 문자열 내부에 특정 문자의 개수를 반환. 대소문자 구별 됨.
print(str1.count('i',0,4)) # 0이상 4미만 까지
print(str)

#find
print(str1)
print(str1.find('p')) # 찾는 문자가 없으면 -1 반환
print(str1.find('i')) # 찾는 문자의 가장 첫번째 인덱스 반환. 
print(str1.rfind('i')) # 찾는 문자의 가장 마지막 인덱스 반환. 
print(str1.find('i',10)) # start index
print(str1.find('i',5,10)) # start & end index
print(str)


# 문자열 대/소문자 변환
print(str1.upper())
print(str1.lower())
print(str1.swapcase()) # 소문자 <-> 대문자 교체
print(str1)
print(str)


print(str1.capitalize()) # 첫글자만 대문자, 나머지는 소문자
print(str1.title()) # 각 단어의 앞문자를 대문자로. 나머지는 소문자
print(str)

# strip
str4 = '   My dog is cute   '
print(str4.strip() + '.') #양쪽 여백 제거
print(str4.lstrip() + '.') #왼쪽 여백 제거
print(str4.rstrip() + '.') #오른쪽 여백 제거
print(str)

#replace
print(str1)
print(str1.replace(' ','-공백-')) 
print(str1.replace(' ','-공백-',1)) #원하는 개수만큼만 변환

#list로 변환
print(list(str1))