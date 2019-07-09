# _*_ conding:utf-8 _*_

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%2s'%(i,j,i*j),end='\t')
#     print()



a = 0
while a<10:
    b = 1
    while b <= a:
        print('%s*%s=%s'%(a,b,a*b),end='\t')
        b += 1
    a += 1
    print()