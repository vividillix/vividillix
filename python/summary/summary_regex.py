# 정규식
import re

p = re.compile('[a-z]+') 
# [] : 이 문자열들중 하나라도 포함이냐
# + : 반복

m = p.match('python') # match가 되는 지 반환 (일치 여부)
m = p.match('3 python') # 얘는 적합하지 않아서 None 반환
print(m)

m = p.search('3 python') # 원하는 p 표현이 포함되는지 반환
print(m)

m = p.findall('life is too short') # 일치하는 부분을 리스트로 반환
print(m) # ['life', 'is', 'too', 'short']

m = p.finditer('life is too short') # 일치하는 부분의 매치값을 반환
for i in m:
    print(i) # 각 match 객체가 출력됨.
    
print('----------')
    
# match 객체의 메서드
# group : 문자열 리턴
# start : 시작 위치 리턴
# end : 끝 위치 리턴
# span : 시작,끝 튜플 리턴

m = p.match('python')
print(m.group())
print(m.start())
print(m.end()) # 포함안하는 인덱스 번호
print(m.span())
print('----------')


# Dotall, S
# dot : 줄 바꿈을 제외한 모든 문자 (최소 1개)

p = re.compile('a.b')
m = p.match('a\nb')
print(m) # None

p = re.compile('a.b', re.DOTALL) # re.DOTALL : 줄바꿈도 인정해줌.
p = re.compile('a.b', re.S) # re.DOTALL 의 약어
m = p.match('a\nb')
print(m) 
print('----------')


# IGNORECATE, I
p = re.compile('[a-z]') # 이건 참고로 시작문자만 체크함.
print(p.match('python')) 
print(p.match('yDthon')) # 결과 나온다 이거지..
print(p.match('PYTHON')) # None

p = re.compile('[a-z]', re.IGNORECASE) # 대소문자 무시
print(p.match('python')) 
print(p.match('yDthon'))
print(p.match('PYTHON'))
print('----------')

# MULTILINE, M
# ^문자열 : 맨 처음에 문자열이 나온다.
# \s : 공백 
# \w : 알파벳, 숫자, _ 중의 한 문자
# + : 반복
p = re.compile('^python\s\w+') # 즉, python이 맨처음 나오고 공백 뒤에 문자들이 반복되어야함.

data = """python o_ne
ddasd
python two
asd
python three
"""

print(p.findall(data)) # python o_ne

p = re.compile('^python\s\w+', re.M) # 꺽새를 첫 문장이 아니어도 맨 앞으로 인정해줌.
print(p.findall(data)) # python o_ne / python two / python three
print('----------')


# VERBOSE, X
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
                     &[#]
                     (
                         0[0-7]+
                         |[0-9]+
                         |x[0-9a-fA-F]+
                         )
                         ;
                         """, re.VERBOSE) # 한줄로 안쓰고 떨어뜨려도 인식해줌.


# 백슬래시 문제

p = re.compile('\section') # \section이라는 문자를 찾고 싶을때 그냥 쓰면 공백 ection 으로 인식됨
m = p.match('\section') # None
m = p.match(' ection') # Match!

p = re.compile('\\section') # 이건 그럼 뭐란 말임?
m = p.match('\section') # None
m = p.match('\\section') # None
m = p.match(' ection') # Match!

p = re.compile('\\\\section') 
m = p.match('\section') # Match!
m = p.match('\\section') # Match!

p = re.compile(r'\\section') 
m = p.match('\section') # Match!
m = p.match('\\section') # Match!
m = p.match(' ection') # None
print('----------')


# 메타 문자
# | : 앞에것 또는 뒤에것과 일치할때
# ^ : 맨앞
# $ : 맨뒤
# \b : 공백

# 컴파일 없이 한방에 쓰는 법
print(re.search('^Life' , 'Life is good')) # Match!
print(re.search('^Life' , 'My Life is good')) #None

print(re.search('\bclass\b' , ' class ')) #None
print(re.search('\bclass\b' , ' sclass ')) #None
print(re.search('\bclass\b' , '\bclass\b ')) # Match! \bclass\b 이만큼이 일치

print(re.search(r'\bclass\b' , ' class ')) #Match!
print(re.search(r'\bclass\b' , ' sclass ')) #None
print(re.search(r'\bclass\b' , '\bclass\b ')) # Match! class 만 일치
print('----------')


# 그룹핑 ()
p = re.compile('ABC+') # 이건 마지막 C가 반복되는걸 찾아줌.
p = re.compile('(ABC)+') # 이건 ABC가 반복되는걸 찾아줌.
m = p.search('well.. ABCABCABC OK?')
print(m)
print(m.group())

p = re.compile(r"(\w+)\s+\d+[-](\d)+[-]\d+") # 대체 이해할 수 없군.
m = p.search("park 010-1234-5678")
print(m.group()) # 이건 그냥 전체고
print(m.group(1)) # 이건 결과중에서 1번째 그룸
print(m.group(2)) # 이건 결과중에서 1번째 그룸

p = re.compile(r'(\b\w+)\s+\1') # \1d은 그룹핑 표현의 결과를 써주는것.
print(p.search('Paris in the the spring').group()) # the the

# 그룹핑에 이름 붙이기 ?P<name>
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-](\d)+[-]\d+)")
m = p.search("park 010-1234-5678")
print(m.group("name"))
print('----------')


# 전방탐색 : 긍정형 (?=)
p = re.compile(".+:") # . (문자)가 +(반복)되다가 : 만나면 매치
m = p.search("http://google.com")
print(m.group()) # http: 

p = re.compile(".+(?=:)") # ?=다음거가 의미는 있지만 출력은 x
m = p.search("http://google.com")
print(m.group()) # http

# 전방탐색 : 부정형 (?!)
p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpt
""")
print(l)

# 문자열 바꾸기 sub
p = re.compile('(blue|white|red)') # 이 단어들을 찾는 다는 그룹
print(p.sub('colour', 'blue socks and red shoes')) # 찾아서 인자1로 바꿔라
print('----------')



# Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
print(re.match('<.*>',s).group()) # Greedy 작은 블록이 아니고 전체를 출력해버림
print(re.match('<.*?>',s).group()) # Non-Greedy
