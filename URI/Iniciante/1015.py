# -*- coding: utf-8 -*-

import math

x1,y1 = input().split(" ")
x2,y2 = input().split(" ")
distancia = math.sqrt(pow(float(x2)-float(x1),2)+ pow(float(y2)-float(y1),2))

print("%0.4f"%distancia)