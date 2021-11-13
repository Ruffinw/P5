c=int(input("Input a number "))
c=c-1
while c!=0:
    k=0
    t=1
    while t<c:
        
        if c%t==0:
            k=k+t              
        t=t+1
         
    if c==k:
        print(c,"Совершенное число,")
    c=c-1  