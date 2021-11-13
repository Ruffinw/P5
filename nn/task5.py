c=int(input("Input число:"))
n=(input("Input ur name:"))

if c<10:
    i=0
    for i in range(c):
        print(n)
        i+=1
else:
    for i in range(3):
        print("Too high")
        i+=1
