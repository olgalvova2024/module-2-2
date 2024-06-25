first=int(input('Введите число '))
second=int(input('Введите число '))
third=int(input('Введите число '))
# 1-ый вариант решения
if first==second and first==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)

# 2-ой вариант решения
i=0
if first==second:
    i=i+1
if first==third:
    i=i+1
if second==third:
    i=i+1
if i==0 or i==3:
    print(i)
else:
    print((i+1))


