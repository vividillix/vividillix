# 금광 문제

# 입력
# t ( 테스트 케이스 개수 )
# n m ( n x m 형태의 금광)
# ... ( 각 금광에 존재하는 금의 개수)

# 금광은 왼 -> 오 방향으로만 진행하고, 위 아래로 이동할 수 있음.

# 가장 많은 금을 갖기 위해서.. 왼쪽 열의 각 칸 중 최대값 + 내 자리 값 인거네.

import time


for tc in range(int(input())):
    # 금광 정보 입력
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    
    start_time = time.time()
    
    # 2차원으로 변환
    dp = []
    for i in range(n):
        dp.append(array[i*m : i*m + m])
    
    # 다이나믹 진행 : dp[i][j] 위치의 값을 구하려고 하는 거임
    for j in range(1,m):
        for i in range(n):
            # 위에서 내려오는 경우
            if i == 0 : up = 0
            else: up = dp[i-1][j-1]
            
            # 아래에서 올라오는 경우
            if i == n-1 : down = 0
            else: down = dp[i+1][j-1]
            
            # 옆에서 오는 경우
            left = dp[i][j-1]
            
            dp[i][j] += max(up,down,left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])    


    end_time = time.time()

    print(result)
    print(end_time - start_time)



# 병사 배치하기

# n : 병사의 수 (1~2000)
# values : 각 병사의 전투력

# 순서는 무작위로 제공 된 것.
# 이제 전투력이 내림 차순이 되도록 일부를 열외 시켜야 함.
# 그러면서 총 전투력은 최대가 되었으면 함.

# 출력은 열외할 병사 수.

        