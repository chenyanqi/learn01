#_*_ conding:uft-8 _*_
print_num = 0
count = 0
while count < 100:
    if count == print_num:
        print(('There you got the number:%s') %(count))
        choice = input('do you want to continue the loop?(y/n)')
        if choice == 'n':
            break
        else:
            while print_num <= count:
                print_num = int(input('which loop do you want it to be print out?'))
                if print_num <= count:
                    print('已经过了，sx!')
    else:
        print('Loop:',count)
    count += 1
else:
    print('loop:',count)