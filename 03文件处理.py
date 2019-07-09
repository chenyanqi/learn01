f = open("E:\python_learn\learn01\\accounts.txt",'r')
for line in f.readline():
    line = line.strip('\n').split(' ')
    print(line)