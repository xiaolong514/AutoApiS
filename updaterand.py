# -*- coding: UTF-8 -*-
import json,sys,time,random
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用
#以下空行不要删除，以便运行时插入机密



















slice1 = [0]*8
randomapi=[1,2,6,7,21,22,29]
list1 = [[3,4,5],[8,9,10,11],[23,24,25,26,27,28],[14,15,16,17],[18,19,20],[12,13]]
list2 = [1,2,2,2,2,2]
path=sys.path[0]+r'/config/randomapi.txt'
path5=sys.path[0]+r'/config/buconfig.txt'
for i in range(0,3):
    slice1[i] = random.sample(list1[i], list2[i])
gk=slice1[0]
randomapi.append(gk[0])
b = random.randint(0,2)
if b == 0:
    slice1[3]=random.sample(list1[5],2)
if b == 1:
    slice1[3]=random.sample(list1[3],2)
if b == 2:
    slice1[3]=random.sample(list1[4],2)
print(str(slice1[1]))
print(str(slice1[2]))
print(str(slice1[3]))
for h in range(1,4):
    gg=slice1[h]
    for h1 in range(0,2):
        gd=gg[h1]
        randomapi.append(gd)

random.shuffle(randomapi)
str2 = ','.join([str(x) for x in randomapi])
with open(path, 'w+') as f:
    f.write(str2)
fe = open(path5, "r+")
rfv = fe.read()
fe.close()
if rfv == 'Y':
    str5 = 'N'
    with open(path5, 'w+') as fn:
        fn.write(str5)
else:
    str5 = 'Y'
    with open(path5, 'w+') as fn:
        fn.write(str5)
