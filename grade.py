

def grade1():
    global grade
    grade = int(input('grade\n'))
grade1()
while grade > 100:
    print('enter real grade')
    grade1()
    
gradez={'A+':100,'A':90,'B':80,'C':70,'D':60}

for x,y in gradez.items():
    if grade < 60:
        print('failed')
        break
    elif y<=grade:
        print(x)
        break
