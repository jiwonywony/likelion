#문제 1번
hurdle=0
for hurdle in range(5):
    print("허들을 넘었습니다.")
    if hurdle == 4:
        print("레이스를 완주했습니다.")

#문제 2번
hurdle=5
while hurdle != 0:
    print("허들이 %d개 남았습니다." %hurdle)
    hurdle = hurdle - 1
    if hurdle == 0:
        print("레이스를 완주했습니다.")

#문제 3번
name = input()
score = int(input())
if score in range(90,101):
    print("%s의 학점 : A"%name)
elif score in range(80,90):
    print("%s의 학점 : B"%name)
elif score in range(70,80):
    print("%s의 학점 : C"%name)
elif score in range(60,70):
    print("%s의 학점 : D"%name)
else:
    print("%s의 학점 : F"%name)

#문제 4번
for i in range(0,4):
    name = input()
    score = int(input())
    if score in range(90,101):
        print("%s의 학점 : A"%name)
    elif score in range(80,90):
        print("%s의 학점 : B"%name)
    elif score in range(70,80):
        print("%s의 학점 : C"%name)
    elif score in range(60,70):
        print("%s의 학점 : D"%name)
    else:
        print("%s의 학점 : F"%name)