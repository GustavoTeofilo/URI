# -*- coding: utf-8 -*-

valores1 = input ().split(' ')
valores2 = input ().split(' ')
cod = int(valores1[0])
cod2 = int(valores2[0])

numero1 = int (valores1[1])
numero2 = int (valores2[1])

unitario = float (valores1[2])
unitario2 = float (valores2[2])

valor = (numero1*unitario)+(numero2*unitario2)

print("VALOR A PAGAR: R$ %0.2F"%valor)