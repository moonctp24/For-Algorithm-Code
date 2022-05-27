'''
Shinhan SCOOLCHECK 코딩챌린저
문제1. 거스름돈
현재 우리나라가 사용하고 있는 1원, 10원 50원 100원 500원 1,000원 5,000원 10,000원 50,000원 권 화폐를 사용
'''

changeMoney = int(input()) # 거스름돈 금액

count = 0 # 거슬러 줄 화페의 총 개수

# 거슬러 줄 돈이 없을 때 까지 반복
while(changeMoney > 0): 
    # print(count, changeMoney)
    if changeMoney >= 50000:
        tmp = int(changeMoney / 50000)
        changeMoney = changeMoney - 50000*tmp
        count = count + tmp
    elif changeMoney >= 10000:
        tmp = int(changeMoney / 10000)
        changeMoney = changeMoney - 10000*tmp
        count = count + tmp
    
    elif changeMoney >= 5000:
        tmp = int(changeMoney / 5000)
        changeMoney = changeMoney - 5000*tmp
        count = count + tmp
        
    elif changeMoney >= 1000:
        tmp = int(changeMoney / 1000)
        changeMoney = changeMoney - 1000*tmp
        count = count + tmp
        
    elif changeMoney >= 500:
        tmp = int(changeMoney / 500)
        changeMoney = changeMoney - 500*tmp
        count = count + tmp
    elif changeMoney >= 100:
        tmp = int(changeMoney / 100)
        changeMoney = changeMoney - 100*tmp
        count = count + tmp
    elif changeMoney >= 50:
        tmp = int(changeMoney / 50)
        changeMoney = changeMoney - 50*tmp
        count = count + tmp
    elif changeMoney >= 10:
        tmp = int(changeMoney / 10)
        changeMoney = changeMoney - 10*tmp
        count = count + tmp
    else:
        tmp = int(changeMoney / 1)
        changeMoney = changeMoney - 1*tmp
        count = count + tmp
        

print(count)