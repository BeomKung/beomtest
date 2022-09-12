n = int(input())
result = n
count = 0

while True:
    a = result // 10
    b = result % 10
    c = (a+b) % 10
    result = (b * 10) + c
    count = count + 1
    if(result == n):
        break

print (count)    
