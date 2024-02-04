'''
제약조건
1. 1 <= s.length <= 10^4
2. s는 괄호만 담겨있다.
'''

# using stack
def isValidParenthesis(s):
    pStack = []
    
    for p in s:
        if(p == '(' or p == '[' or p == '{'):
            pStack.append(p)
        else:
            tmpP = pStack.pop()
            if(p == ')' and tmpP != '('):
                return False
            elif(p == '}' and tmpP != '{'):
                return False
            elif(p == ']' and tmpP != '['):
                return False
    if(len(pStack)==0):
        return True
    else:
        return False

print(isValidParenthesis('(({}[]))'))
print(isValidParenthesis('(({}[{]))'))
print(isValidParenthesis('(({}[]())'))