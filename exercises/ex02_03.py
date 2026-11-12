a = int(input())
hour = a//3600
a1 = a%3600
minutes = a1//60
sec = a1%60
print(hour, minutes, sec, sep=' : ')

b = int(input())
day = b//86400
b1 = b%86400
hour = b1//3600
b2 = b1%3600
minute = b2//60
sec = b2%60
print(day, hour, minute, sec, sep=':')

total = int(input())
page_size = int(input())
num_page = (total-1)//page_size+1
print(num_page)

num = int(input())
a = num//10
b = num%10
print(b, a, sep='')

price = int(input())
dol = price//100
cent1 = price%100//10
cent2 = price%10
print(dol, '.', cent1, cent2, sep='')