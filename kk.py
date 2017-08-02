# -*- coding: utf-8 -*-
#python kk.py
import itchat
from itchat.content import *

who_send = None
@itchat.msg_register(TEXT)
def fw_ice(msg):
	global who_send
	msg_text = msg['Text']
	who_send = msg['FromUserName']
	itchat.send(msg_text, xiaoice)

@itchat.msg_register(TEXT, isMpChat=True)
def get_ice(msg):
	ice_msg = msg['Text']
	itchat.send(ice_msg, toUserName=who_send)


itchat.auto_login(enableCmdQR=True,hotReload=True)
xiaoice = itchat.search_mps(name='小冰')[0]['UserName']
itchat.run()

