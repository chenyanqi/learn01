# name = ['!','#','wang','gen',2,'c','1',2,'nihao','zhongguo','d',1,2,3,4,5,6,7]
# first_pos = 0
# for i in range(name.count(2)):
#     new_list = name[first_pos:]
#     next_pos = new_list.index(2) + 1
#     print('Find pos:',first_pos + new_list.index(2))
#     first_pos += next_pos

a = [1,2,3,4,5,6,7,7,2,3,4,5,2,4,2,4,65,2,6,56,6,7,7,3,34,3]
pos = 0
for i in range(a.count(2)):
    if pos == 0:
        pos = a.index(2)
    else:
        pos = a.index(2,pos+1)
    print(pos)