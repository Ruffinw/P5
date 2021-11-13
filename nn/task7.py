q=int(input("В каком направление вы хотите вести отсчёт(1-прямой,2-обратный)"))

if q==1:
    t=int(input("Input number:"))
    i=1
    for i in range(t):
        print(i)
        i+=1
    print(i)    
elif q==2:
    y=int(input("Input number меньше 20:"))      
    i=20
    while i>=y:
        print(i)
        i-=1
else:
    print("I dont understand")        