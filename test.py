import itchat
from itchat.content import *
'''@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
'''
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, SYSTEM], isMpChat=True)
def text_reply(msg):
    print('%s' % msg['FromUserName'])

itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()