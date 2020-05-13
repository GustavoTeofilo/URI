age = int(input())

year = age//365
month =(age%365)//30
day = (age%365)%30

print(year,"ano(s)")
print(month,"mes(es)")
print(day,"dia(s)")
