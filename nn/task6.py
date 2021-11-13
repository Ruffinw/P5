total=0
i=0
for i in range(5):
    c=int(input("Input number:"))
    ans=int(input("Хотите ли вы включить это число в суммирование(1-Да,2-Нет):"))
    if ans==1:
        total=total+c
    i+=1    
print(total)   
