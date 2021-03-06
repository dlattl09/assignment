# -*- coding: utf-8 -*-
"""knapsack_problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h-BRCRCgLHcjz-evHfG4BHxubauvHKD1

# 0-1 KnapSack Problem
"""

# 필요한 라이브러리 import
import numpy as np
import timeit
import copy

"""### 퀵정렬 구현(다차원)"""

def quickSort(array, index): # 다차원 배열 quicksort
    left=[]
    center=[]
    right=[]
    if len(array) in [0,1]:      # 배열 비어있을 경우 리턴
        return array
    pivot=array[0][index]        # 다차원 배열의 원하는 index를 pivot으로 지정해줌
    for i in array:
        if i[index]<pivot:   
            left.append(i)
        elif i[index]>pivot:
            right.append(i)
        else:
            center.append(i)    
    return quickSort(right,index)+center+quickSort(left,index) # 다차원 배열 내림차순으로 정렬

"""### Dynamic programming"""

#동적계획법으로 배낭문제 해결하기
def KnapSack_DP(num, weight, profit, M):
    start_time=timeit.default_timer()                                               # 시작 시간 측정
    max_profit = [[0 for x in range(M+1)] for x in range(num+1)]        # max_profit 값 초기화
    
    for i in range(num+1): 
        for w in range(M+1): 
            if i==0 or w==0:               
                max_profit[i][w] = 0                                                  # 물건 또는 무게=0일 때 max_profit 초기화
                
            elif weight[i-1] <= w:                                                   # weight값이 배낭크기(w)보다 작을 때
                
                # 물건을 넣었을 때와 안넣었을 때의 profit값 중 더 큰거 선택
                max_profit[i][w] = max(profit[i-1] + max_profit[i-1][w-weight[i-1]],  max_profit[i-1][w])               
            else:
            
                max_profit[i][w] = max_profit[i-1][w]       #물건 (wi) 배낭에 집어넣지 않음
                
    x_vector=[0]*num                                                                # 해벡터 초기화
    result=max_profit[num][M]                                                        
    capacity=M                                                                        
    
    for i in range(num,0,-1):
        if result==profit[i-1] + max_profit[i-1][capacity-weight[i-1]]:         # 물건(i)이 집어넣어진 경우
            x_vector[i-1] = 1                                                         # 해벡터에 추가
            
            result -= profit[i-1]                                                         # 추가된 물건만큼 이윤 감소
            capacity -= weight[i-1]                                                # 추가된 물건만큼 무게 감소
    end_time=timeit.default_timer()
    total_time=(end_time-start_time)*(10**3)                                 # 종료 시간 측정 후 millisec로 저장

    print('(1) Dynamic Programming')
    print('   The maximum profit is $',str(max_profit[num][M]))
    print('   The solution vector X  = ',tuple(x_vector))
    print('   The execution time is ','%.2f' %(total_time),'milliseconds\n\n')

"""### Backtracking"""

def promising(i,profit,weight):                                       # promising 한지 검사
    j=0
    k=0
    twotal=0                                                               # 배낭에 넣은 물건의 무게 합 초기화
    bound=0                                                              # 최대 이윤 상한선 초기화
    if(weight>=knapsack_cap):                                       
        return False
    else :
        j = i 
        bound = profit                                                  
        wtotal=weight
        while(j<=(num_obj-1) and wtotal+w[j]<=knapsack_cap):  # k까지 물건을 완전히 배낭에 집어넣음
            wtotal = wtotal + w[j]
            bound = bound + p[j]
            j = j + 1
        k=j                # k: 용량을 처음으로 초과하는 물건 ->남아있는 비율만큼만 넣을 수 있음
        if(k<=num_obj-1):
            bound = bound + (knapsack_cap - wtotal)*(p[k]/w[k])  # 남은 배낭 용량을 물건 p/w만큼 채워넣음
        return bound>maxprofit                                           #최대 이윤 상한선(bound)>maxprofit일 떄 true 값 리턴

def knapsack(i,profit,weight):
    global maxprofit                                                         # 현재까지의 최대 이윤 전역변수로 지정
    global best, x_vector                                                    # 해벡터 전역변수로 지정
    if(i<num_obj):
        if(weight<=knapsack_cap and profit > maxprofit):           
            maxprofit = copy.deepcopy(profit)                           # max_profit값 업데이트
            best = copy.deepcopy(x_vector)                              # max_profit을 만드는 해벡터
        if(promising(i,profit,weight)):                                       # promising할 때 ->preorder로 진행됨
            x_vector[i] = 1                                                     # wi가 해에 포함될 때
            knapsack(i+1,profit+p[i],weight+w[i])
            x_vector[i] = 0                                                     # wi가 해에 포함되지 않을 때
            knapsack(i+1,profit,weight)

file_num=1
for i in range(7):
    file=open('C:\\p2data\\p2data'+str(i)+'.txt','rt')
    read=file.read()
    split=read.split()                   # 파일을 리스트(문자열)로 읽어오기
    split=[int (n) for n in split]       # 읽어온 리스트를 정수형으로 변환

    num_obj=split[0]                     # 물건 개수
    profit=[]                                # pi  : 각 물건에 대한 이윤
    weight=[]                              # wi  : 각 물건에 대한 무게
    p_per_w=[]                            # pi/wi
    
    p_index = 1
    w_index = 1+num_obj
    
    for i in range(num_obj):
        profit.append(split[p_index])       # profit 리스트에 파일의 profit 값들 추가
        weight.append(split[w_index])       # weight 리스트에 파일의 weight 값들 추가
        p_per_w.append(profit[i]/weight[i])   # p_per_w 리스트에 profit/weight 값들 추가

        p_index +=1
        w_index +=1

    knapsack_cap=split[len(split)-1]      # 배낭크기(knapsack capacity)

    print(str(file_num)+'.knap-'+str(file_num)+'.txt')
    print('  n = '+str(num_obj))
    print('  pi =',' '.join([str(i) for i in profit]))                    # 각 리스트의 요소를 문자열로 출력
    print('  wi =',' '.join([str(i) for i in weight]))
    print('  pi/wi =',' '.join([str('%.1f' % i) for i in p_per_w]))  # pi/wi값 소수 첫째짜리까지 표기
    print('  M = '+str(knapsack_cap),'\n\n')

    file_num+=1
    x_vector = [0]*num_obj                                         # 해 vector 초기화
    maxprofit=0                                                       # max_profit 값 초기화
    best = []                                                            # best : 최대이윤을 결정하는 해벡터
    index = [0]*num_obj
    for i in range(num_obj):
        index[i]=i                                                       # 각 리스트의 초기 index값을 저장하는 리스트

    # Dynamic programming    
    KnapSack_DP(num_obj, weight, profit, knapsack_cap)

    # BackTracking programming
    start_time=timeit.default_timer()                             # 시작 시간 측정

    pack=np.transpose(np.array([p_per_w,profit,weight,index]))    # profit/weight, profit, weight값을 가진 다차원 리스트
                                                                                   #  행과 열 바꾸기
    pack_sorted = np.transpose(quickSort(pack, 0))                  # profit/weight을 기준으로 퀵정렬한 후, 다시 행열 바꿔줌
    
    p, w, per, index = pack_sorted[1], pack_sorted[2], pack_sorted[0], pack_sorted[3] 

    knapsack(0,0,0)                                                    # 백트레킹 호출
    
    end_time=timeit.default_timer()
    total_time=(end_time-start_time)*(10**3)                   # 종료 시간 측정 후 milisec로 저장
    
    pack=np.transpose(np.array([index,best]))          # best를 해벡터의 초기 index값을 저장하는 리스트(index)와 묶어줌               
    pack_sorted_reverse = np.transpose(quickSort(pack, 0))    # 행/열을 변환한 다차원 리스트 pack을 퀵정렬 후 원상복구
    best=list(map(int,pack_sorted_reverse[1][::-1]))           # best->원래 인덱스 순서 가짐(float을 int로 변환)
  
    print('(2) Backtracking Programming')
    print('   The maximum profit is $',int(maxprofit))
    print('   The solution vector X  = ',tuple(best))
    print('   The execution time is ','%.2f' %(total_time),'milliseconds\n\n\n')



