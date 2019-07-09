# real_name = 'zhangsan'
# real_passwd = '123456'
# name = input('please input your name:')
# password = input('please input your password')
# if real_name == name and real_passwd == password:
#     print('welcome to mimi')
# else:
#     print('is not real')

#for循环登陆
# real_name = 'zhangsan'
# real_passwd = '123456'
# count = 0;
# for i in range(3):
#     username = input("username:")
#     password = input("password:")
#     if username == real_name and password == real_passwd:
#         print('welcom to mimi')
#         count = 3
#         break
#     else:
#         print("please input the real infomation！")
#         count += 1
#         print('you can try',2 -i, 'times')

#while循环登陆
# user = "123"
# password = "1"
# count = 0;
# while count < 3:
#     username = input("username:")
#     passwd = input("password:")
#     if username == user and password == passwd:
#         print("Welcome Login")
#     else:
#         print("Wrong username or password")
#         count += 1
#         print("you can try", 3 - count, "times")


#练习
import  sys
retry_limit = 1
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count <= retry_limit:
    username = input('Username: ')
    lock_check = open(lock_file)

    for line in lock_check.readlines():
        line = line.split()
        if username == line[0]:
        #if username in line:
            sys.exit('User %s is locaked!' % username)
    password  = input('Password: ')
    f = open(account_file,'rb')
    match_flag = False
    for line in f.readlines():
        user,passwd = line.decode('utf8').strip('\n').split()
        if username == user and password == passwd:
            print('Match,%s' % username)
            match_flag = True
            break
    f.close()
    if match_flag == False:
        print('User unmatched!')
        retry_count += 1
    else:
        print('Welcome login system')
        break
else:
    print('Your account is locked!')
    f = open(lock_file,encoding='utf-8',mode='a')
    f.write(username + '\n')
    f.close




