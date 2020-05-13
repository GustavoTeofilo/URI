n100=float(100)
n50=float(50)
n20 = float(20)
n10 = float(10)
n5 = float(5)
n2 = float(2)

m1 = float(1)
m50 = 0.50
m25 = 0.25
m10 = 0.10
m50 = 0.50
m01 = 0.01
m5 = 0.05

num = float(input())

print('NOTAS:')
print(int(num//n100),'nota(s) de R$ %0.2f'%n100)
num = num%n100

print(int(num//n50),'nota(s) de R$ %0.2f'%n50)
num = num%n50

print(int(num//n20),'nota(s) de R$ %0.2f'%n20)
num = num%n20

print(int(num//n10),'nota(s) de R$ %0.2f'%n10)
num = num%n10

print(int(num//n5),'nota(s) de R$ %0.2f'%n5)
num = num%n5

print(int(num//n2),'nota(s) de R$ %0.2f'%n2)
num = num%n2

print('MOEDAS:')

print(int(num//m1),'moeda(s) de R$ %0.2f'%m1)
num = num%m1

print(int(num//m50),'moeda(s) de R$ %0.2f'%m50)
num = num%m50

print(int(num//m25),'moeda(s) de R$ %0.2f'%m25)
num = num%m25

print(int(num//m10),'moeda(s) de R$ %0.2f'%m10)
num = num%m10

print(int(num//m5),'moeda(s) de R$ %0.2f'%m5)
num = num%m5

print(int(num//m01),'moeda(s) de R$ %0.2f'%m01)
num = num%m01
