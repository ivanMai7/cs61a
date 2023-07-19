n = 12345
li = []
tmp = n
while(tmp > 0):
    li = [tmp % 10] + li
    tmp = tmp // 10
print(li)
    