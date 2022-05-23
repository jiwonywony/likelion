#문제 1번
def plus(num1,num2):     
    return num1+num2

def minus(num1,num2):    
    return num1-num2

def multiply(num1,num2): 
    return num1*num2

def division(num1,num2): 
    return num1/num2

while(True):
    num1, num2 = map(int,input("연산을 진행할 두 숫자를 입력하시오 : ").split(" "))
    i= input("어떠한 연산을 수행할까요? ")

    if(i == '+'):
        plus(num1,num2)
    elif(i == '-'):
        minus(num1,num2)
    elif(i == '*'):
        multiply(num1,num2)
    elif(i == '/'):
        division(num1,num2)
    else:
        print("해당 연산은 지원하지 않습니다.")


#문제 2번
import random
import time

def lotto():
    number = random.sample(range(1,46),6)
    number.sort()
    for i in range(1,6):
        print("%d ..."%i)
        a = time.sleep(2)
    print("로또번호는!!")
    print(number)

while(True):
    a = input("로또번호 추출을 시작합니까?(y/n) :")
    if a == "y":
        print("번호 추출중...")
        lotto()
    else:
        print("로또 추출을 종료합니다.")