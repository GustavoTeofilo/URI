# -*- coding: utf-8 -*-

A,B,C =input().split(' ')

maior=(int(A)+int(B)+abs(int(A)-int(B)))/2
f = (maior+int(C)+abs(maior-int(C)))/2
print("%0.0f eh o maior"%f)