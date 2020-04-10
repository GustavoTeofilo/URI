# -*- coding: utf-8 -*-

nome = input()
salariof = float(input())
vendas = float(input())
pvendas = (vendas*15)/100
salario = salariof + pvendas

print("TOTAL = R$ %0.2f"%salario)