# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time,random

dd2=[1]
id_list2=[1]

def gettoken(refresh_token):
    headers={'Content-Type':'application/x-www-form-urlencoded'
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
    with open(path, 'w+') as f:
        f.write(refresh_token)
def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    access_token=gettoken(refresh_token)
for a in range(0, len(id_list)):
    path=sys.path[0]+r'/token/'+str(a)+'.txt'
    id_lists=id_list
    secret_lists=secret_list
    main()
if id_list2 != dd2:
    for a in range(0, len(id_list2)):
        path=sys.path[0]+r'/backuptoken/'+str(a)+'.txt'
        id_lists=id_list2
        secret_lists=secret_list2
        main()
