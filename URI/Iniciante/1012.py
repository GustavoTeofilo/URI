# -*- coding: utf-8 -*-

A,B,C =input().split(' ')

triangulo = float(A)*float(C)/2
circulo = 3.14159*float(C)**2
trapezio = (float(A)+float(B))/2*float(C)
quadrado = float(B)**2
retangulo = float(A)*float(B)

print("TRIANGULO: %0.3f"%triangulo)
print("CIRCULO: %0.3f"%circulo)
print("TRAPEZIO: %0.3f"%trapezio)
print("QUADRADO: %0.3f"%quadrado)
print("RETANGULO: %0.3f"%retangulo)