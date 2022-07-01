import re
 


def sol(path):
    answer = []    
    
    time = 0
    dir = path[0]
    
    while len(path) > 0:
        print(dir)
        str1 = path[0] + '+'
        
        p = re.compile(str1) 
        m = p.match(path) # match가 되는 지 반환 (일치 여부)
        
        
        if m != None:
            cnt = m.end() # 같은 글자 수
            # 매치된 글자수랑 남은 거리랑 똑같으면 종료
            if cnt == len(path) :
                break
                
            # 매치 된 값이 6개 이상이면 거리 플러스만 하고 하나 제거.
            if cnt > 5:
                path = path[1:]
                time += 1
                
            # 매치 된 값이 5개 이하이면
            else:
                result = ''
                
                path = path[cnt:]
                
                # 방향 판단
                next_dir = path[0]

                result += "Time " + str(time)
                result += ": Go straight " + str(cnt*100)
                
                # 왼쪽
                if (dir,next_dir) in [('E','N'),('S','E'),('N','W'),('W','S')]:
                    result += "m and turn left"
                else:
                    result += "m and turn right"
                
                time += cnt
                
                dir = next_dir
                
                answer.append(result)
            
        
    
    return answer


# print(sol("EEEEEEN"))


def sol2(call):

    # 단일 문자의 개수를 세고. 최대 크기인 문자들 다 지우기.
    low_call = call.lower()
    list_call = list(low_call)
    
    max_cnt = 0
    pattern = []
    
    for i in set(list_call):
        cnt = list_call.count(i)
        list_call.remove(i)
        
        print(i,' ',cnt)
        
        if cnt > max_cnt:
            max_cnt = cnt
            pattern = []
            pattern.append(i)
        elif cnt == max_cnt:
            pattern.append(i)
            
    print(pattern)
            
    # 이제 쟤네 지우기
    for i in pattern:
        call = call.replace(i,"")
        call = call.replace(i.upper(),"")

    
    
    return call

# print(sol2("abcabcdefabc"))


def sol3(tstring, variables):
    answer = ''
    
    # var 에 무한 반복이 있는지 찾고. 그렇다면 제거하기
    
    keys = [ x[0] for x in variables]
    vals = [ x[1] for x in variables]
     
     
    print(keys)
    print(vals)
    
    for v in variables:
        print(v)
        print()
        route = []  # 무한 반복되는 애들 집합
        route.append(v)
        
        key = v[0]
        value = v[1]
        
        while True:
            # 내 결과값이 다시 키에 존재한다면
            if value[1:-1] in keys:
                idx = keys.index(value[1:-1])
                route.append(variables[idx])
                print(idx)

                key = keys[idx]
                value = vals[idx]
                
                print(key)
                
                print(value)
                print()
                
                if v[0] == value[1:-1]:
                    print("무한 반복이라는 것이다0!!")
                    # 경로에 있는 애들 다 지워버리기.
                    for r in route:
                        variables.remove(r)
                    break
                
            else:
                break
    
    print(tstring)
    print(variables)

    for a in range(len(variables)):

        for i in variables:
            tstring = tstring.replace('{'+i[0]+'}', i[1])
        print(tstring)
        print()
    
    return tstring


# print(sol3("this is {template} {template} is {state}", [["a", "{b}"], ["b", "{c}"], ["c", "{a}"]]))
print(sol3("{a} {b} {c} {d} {i}", [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))