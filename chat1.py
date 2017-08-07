# -*- coding: utf-8 -*-
#coding=utf8
import requests
import itchat
import time
from itchat.content import *

KEY = '1107d5601866433dba9599fac1bc0083'
gaoyuan=''
SINCERE_WISH = u'%s,来聊天吧！'
who_send = None
def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot235',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


@itchat.msg_register(TEXT)
def tuling_reply(msg):
    who_send = msg['FromUserName']
    if who_send == gaoyuan:
        #测试SINCERE_WISH内容
        if msg['Text']=='test':
            return (SINCERE_WISH % u'高原')
        
        '''
        #测试功能
        if msg['Text']=='test1':
            print(msg['User']['NickName'])
            return (SINCERE_WISH % u'高原')
        '''

        #变更SINCERE_WISH
        if msg['Text'][:7]=='change:':
            change_word=msg['Text'][7:]
            #print(change_word)
            #return change_word
            global SINCERE_WISH
            SINCERE_WISH=u'%s,'+change_word
            return 'changed '+change_word
        #群发信息SINCERE_WISH
        if msg['Text'][:5]=='send:':
            chatroomName=msg['Text'][5:]
            itchat.get_chatrooms(update=True)
            chatrooms = itchat.search_chatrooms(name=chatroomName)
            #print(chatrooms)
            if chatrooms == []:
                return(u'没有找到群聊：' + chatroomName)
            else:
                chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
                for friend in chatroom['MemberList']:
                    friend = itchat.search_friends(userName=friend['UserName'])
                     # 如果是演示目的，把下面的方法改为print即可
                    itchat.send(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
                    time.sleep(.5)
                return 'send over'
        #return 'yes'#管理账号默认回复
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试

    #存储文字信息 try
    place = r'/'+msg['User']['NickName']+r'.txt'
    #print(place)
    with open(place, 'a') as f:
        localtime = time.asctime( time.localtime(time.time()) )
        f.write(localtime+' \n')
        f.write(msg['User']['NickName']+':'+msg['Text']+' \n')
        f.write(localtime+' \n')
        f.write('爱里寿'+':'+reply+' \n')


#localtime = time.asctime( time.localtime(time.time()) )
#print "本地时间为 :", localtime


    return reply or defaultReply

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
 
'''
@itchat.msg_register(SHARING)
def text_reply(msg):
    friendList = itchat.get_friends(update=True)[1:]
    for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
        itchat.send(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
        #print('ok')
        time.sleep(.5) 
'''

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def fw_ice(msg):
    global who_send
    who_send = msg['FromUserName']
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), xiaoice)

@itchat.msg_register(TEXT, isMpChat=True)
def get_ice(msg):
    ice_msg = msg['Text']
    itchat.send(ice_msg, toUserName=who_send)

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(enableCmdQR=True,hotReload=True)

gaoyuan = itchat.search_friends(name=u'高原')[0]['UserName']
xiaoice = itchat.search_mps(name='小冰')[0]['UserName']

itchat.run()