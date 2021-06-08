# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time,random
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用
#以下空行不要删除，以便运行时插入机密

id_list2 = [1]
secret_list2 = [1]

config_list = {'每次轮数':6,
	       '是否启动随机时间':'Y','延时范围起始':600,'结束':1200,
	       '是否开启随机api顺序':'Y',
	       '是否开启各api延时':'N','api延时范围开始':2,'api延时结束':5,
	       '是否开启各账号延时':'Y','账号延时范围开始':60,'账号延时结束':120,
	       '是否开启备用应用':'N','是否开启测试':'N'}

num1 = [0]*len(id_list)
path2=sys.path[0]+r'/config/randomapi.txt'
path3=sys.path[0]+r'/config/buconfig.txt'
rapi = {'1':r'https://graph.microsoft.com/v1.0/me/',
	'2':r'https://graph.microsoft.com/v1.0/users',
	'3':r'https://graph.microsoft.com/v1.0/me/people',
	'4':r'https://graph.microsoft.com/v1.0/groups',
	'5':r'https://graph.microsoft.com/v1.0/me/contacts',
	'6':r'https://graph.microsoft.com/v1.0/me/drive/root',
	'7':r'https://graph.microsoft.com/v1.0/me/drive/root/children',
	'8':r'https://graph.microsoft.com/v1.0/drive/root',
	'9':r'https://graph.microsoft.com/v1.0/me/drive',
	'10':r'https://graph.microsoft.com/v1.0/me/drive/recent',
	'11':r'https://graph.microsoft.com/v1.0/me/drive/sharedWithMe',
	'12':r'https://graph.microsoft.com/v1.0/me/calendars',
	'13':r'https://graph.microsoft.com/v1.0/me/events',
	'14':r'https://graph.microsoft.com/v1.0/sites/root',
	'15':r'https://graph.microsoft.com/v1.0/sites/root/sites',
	'16':r'https://graph.microsoft.com/v1.0/sites/root/drives',
	'17':r'https://graph.microsoft.com/v1.0/sites/root/columns',
	'18':r'https://graph.microsoft.com/v1.0/me/onenote/notebooks',
	'19':r'https://graph.microsoft.com/v1.0/me/onenote/sections',
	'20':r'https://graph.microsoft.com/v1.0/me/onenote/pages',
	'21':r'https://graph.microsoft.com/v1.0/me/messages',
	'22':r'https://graph.microsoft.com/v1.0/me/mailFolders',
	'23':r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories',
	'24':r'https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta',
	'25':r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
	'26':r"https://graph.microsoft.com/v1.0/me/messages?$filter=importance eq 'high'",
	'27':r'https://graph.microsoft.com/v1.0/me/messages?$search="hello world"',
	'28':r'https://graph.microsoft.com/beta/me/messages?$select=internetMessageHeaders&$top',
        '29':r'https://api.powerbi.com/v1.0/myorg/apps'}
rapi2 = {'1':r'https://graph.microsoft.com/v1.0/me/drive/root',
	 '2':r'https://graph.microsoft.com/v1.0/me/drive',
	 '3':r'https://graph.microsoft.com/v1.0/drive/root',
	 '4':r'https://graph.microsoft.com/v1.0/users',
	 '5':r'https://graph.microsoft.com/v1.0/me/messages',
	 '6':r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
	 '7':r'https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta',
	 '8':r'https://graph.microsoft.com/v1.0/me/drive/root/children',
	 '9':r'https://graph.microsoft.com/v1.0/me/mailFolders',
	 '10':r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories',
	 '11':r'https://api.powerbi.com/v1.0/myorg/apps'}
fc = open(path2, "r+")
randapi = fc.read()
fc.close()
fh = open(path3, "r+")
buconfig = fh.read()
fh.close()
randomapi = randapi.split(',')
def gettoken(refresh_token,a):
    headers={'Content-Type':'application/x-www-form-urlencoded',
	     'Host': 'https://login.microsoftonline.com'
            }
    data={'grant_type': 'refresh_token',
          'refresh_token': refresh_token,
          'client_id':id_lists[a],
	  'scope':'offline_access%20User.ReadWrite.All%20User.Read.All%20Sites.ReadWrite.All%20Sites.Read.All%20MailboxSettings.ReadWrite%20MailboxSettings.Read%20Mail.ReadWrite%20Mail.Read%20Files.ReadWrite.All%20Files.Read.All%20Directory.ReadWrite.All%20Directory.Read.All',
          'client_secret':secret_lists[a],
          'redirect_uri':'http://localhost:53682/'
         }
    html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token',data=data,headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    return access_token
def testapi(path,a,ls):
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    localtime = time.asctime( time.localtime(time.time()) )
    access_token=gettoken(refresh_token,a)
    headers={
    'Authorization':access_token,
    'Content-Type':'application/json'
    }
    print('账号 '+str(a)+'\n第 '+str(ls)+' 轮运行开始时间为 :', localtime)
    if config_list['是否开启随机api顺序'] == 'Y':
        print('总api数13个，请自行确认个数')
        for ra in range(14):
            rana = str(randomapi[ra])
            try:
                if req.get(rapi[rana],headers=headers).status_code == 200:
                    num1[a]+=1
                    print("账号"+str(a)+"的"+rana+"号api调用成功,所有api总成功"+str(num1[a])+'次')
                    if config_list['是否开启各api延时'] != 'N':
                        gg = random.randint(config_list['api延时范围开始'],config_list['api延时结束'])
                        time.sleep(gg)
            except:
                print("pass")
                pass
    else:
        print('总api数10个，请自行确认个数')
        for ra in range(1,12):
            rana = str(ra)
            try:
                if req.get(rapi2[rana],headers=headers).status_code == 200:
                    num1[a]+=1
                    print("账号"+str(a)+"的"+rana+"号api调用成功,所有api总成功"+str(num1[a])+'次')
                    if config_list['是否开启各api延时'] != 'N':
                        gg = random.randint(config_list['api延时范围开始'],config_list['api延时结束'])
                        time.sleep(gg)
            except:
                print("pass")
                pass
def testapi2(path,a,ls):
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    localtime = time.asctime( time.localtime(time.time()) )
    access_token=gettoken(refresh_token,a)
    headers={
    'Authorization':access_token,
    'Content-Type':'application/json'
    }
    print('账号 '+str(a)+' 备用应用\n第 '+str(ls)+' 轮运行开始时间为 :', localtime)
    if config_list['是否开启随机api顺序'] == 'Y':
        print('总api数13个，请自行确认个数')
    else:
        print('总api数10个，请自行确认个数')
    if config_list['是否开启随机api顺序'] == 'Y':
        for ra in range(14):
            rana = str(randomapi[ra])
            try:
                if req.get(rapi[rana],headers=headers).status_code == 200:
                    num1[a]+=1
                    print("账号"+str(a)+"备用的"+rana+"号api调用成功,所有api总成功"+str(num1[a])+'次')
                    if config_list['是否开启各api延时'] != 'N':
                        gg = random.randint(config_list['api延时范围开始'],config_list['api延时结束'])
                        time.sleep(gg)
            except:
                print("pass")
                pass
    else:
        for ra in range(1,12):
            rana = str(ra)
            try:
                if req.get(rapi2[rana],headers=headers).status_code == 200:
                    num1[a]+=1
                    print("账号"+str(a)+"备用的"+rana+"号api调用成功,所有api总成功"+str(num1[a])+'次')
                    if config_list['是否开启各api延时'] != 'N':
                        gg = random.randint(config_list['api延时范围开始'],config_list['api延时结束'])
                        time.sleep(gg)
            except:
                print("pass")
                pass
def main():
    if config_list['是否启动随机时间'] == 'Y':        
        for ls in range(config_list['每次轮数']): 
            b=random.randint(config_list['延时范围起始'],config_list['结束'])
            time.sleep(b)
            for a in range(0, len(id_lists)):
                if config_list['是否开启各账号延时'] == 'Y':
                    c = random.randint(config_list['账号延时范围开始'],config_list['账号延时结束'])
                    time.sleep(c)
                path=sys.path[0]+r'/token/'+str(a)+'.txt'
                testapi(path,a,ls)
    else:
        for ls in range(config_list['每次轮数']): 
            for a in range(0, len(id_lists)):
                if config_list['是否开启各账号延时'] == 'Y':
                    c = random.randint(config_list['账号延时范围开始'],config_list['账号延时结束'])
                    time.sleep(c)
                path=sys.path[0]+r'/token/'+str(a)+'.txt'
                testapi(path,a,ls)
def main2():
    if config_list['是否启动随机时间'] == 'Y':        
        for ls in range(config_list['每次轮数']): 
            b=random.randint(config_list['延时范围起始'],config_list['结束'])
            time.sleep(b)
            for a in range(0, len(id_lists)):
                if config_list['是否开启各账号延时'] == 'Y':
                    c = random.randint(config_list['账号延时范围开始'],config_list['账号延时结束'])
                    time.sleep(c)
                path=sys.path[0]+r'/backuptoken/'+str(a)+'.txt'
                testapi2(path,a,ls)
    else:
        for ls in range(config_list['每次轮数']): 
            for a in range(0, len(id_lists)):
                if config_list['是否开启各账号延时'] == 'Y':
                    c = random.randint(config_list['账号延时范围开始'],config_list['账号延时结束'])
                    time.sleep(c)
                path=sys.path[0]+r'/backuptoken/'+str(a)+'.txt'
                testapi2(path,a,ls)

if config_list['是否开启测试'] == 'Y':
    config_list = {'每次轮数':1,'是否启动随机时间':'N','延时范围起始':600,'结束':1200,'是否开启随机api顺序':'Y','是否开启各api延时':'N','api延时范围开始':2,'api延时结束':5,'是否开启各账号延时':'N','账号延时范围开始':60,'账号延时结束':120,'是否开启备用应用':'N','是否开启测试':'N'}
    id_lists=id_list
    secret_lists=secret_list
    main()
    if id_list2 != [1]:
        id_lists=id_list2
        secret_lists=secret_list2
        main2()
else:
    if config_list['是否开启备用应用'] == 'Y':
        if buconfig == 'Y':
            id_lists=id_list
            secret_lists=secret_list
            main()
        else:
            if id_list2 == [1]:
                id_lists=id_list
                secret_lists=secret_list
                main()
            else:
                id_lists=id_list2
                secret_lists=secret_list2
                main2()
    else:
        id_lists=id_list
        secret_lists=secret_list
        main()
