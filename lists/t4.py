a = input("Введите название блюда: ")
b = input("Введите название блюда: ")
c = input("Введите название блюда: ")
x = input("Введите название блюда: ")
bl = {1:a,2:b,3:c,4:x}
print(bl)
q = int(input("Введите номер блюда которое вы хотели бы исключить: "))
del bl[q]
print(bl)