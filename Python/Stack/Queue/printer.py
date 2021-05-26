'''
https://programmers.co.kr/learn/courses/30/parts/12081
PROGRAMMERS STACK/QUEUE PRINTER
'''

def solution(priorities, location):
    printer = priorities.copy()
    order = [x for x in range(len(priorities))]
    
    i = 0
    while True:
        if printer[i] < max(printer[i+1:]):
            printer.append(printer.pop(i))
            order.append(order.pop(i))
        else: i+=1
        
        if i >= len(printer)-1: break
    
    answer = order.index(location)+1
    return answer

def main():
    priorities1 = [2, 1, 3, 2]
    priorities2 = [1, 1, 9, 1, 1, 1]

    location1 = 2
    location2 = 0

    result1 = 1
    result2 = 5

    if solution(priorities1, location1) == result1: print("RIGHT1")
    if solution(priorities2, location2) == result2: print("RIGHT2")

if __name__=="__main__":
    main()