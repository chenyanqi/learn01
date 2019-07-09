'''
xun

sum = 0
for i in range(10):
    sum += i
    if sum == 21:
        print(i)
        break
    # else:
    #     print(sum)




count = 0
while 1:
    a = input('你服不服？')
    if a == '服：
        breadk
    elif a == '不服':
        count += 1

'''


li = [100,98,85,102,33,52,456,23,55,2]
i = 0

while i < len(li):
    j = i+1
    while j < len(li):
        if li[i] > li[j]:
            li[i],li[j] = li[j],li[i]
        j += 1
    i += 1

print(li)
