# -*- coding: utf-8 -*-
#coding=utf8


        #群发信息SINCERE_WISH
        if msg['Text'][:5]=='send:':
            chatroomName=[5:]
            itchat.get_chatrooms(update=True)
            chatrooms = itchat.search_chatrooms(name=chatroomName)
            if chatrooms is None:
                return(u'没有找到群聊：' + chatroomName)
            else:
                chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
                for friend in chatroom['MemberList']:
                    friend = itchat.search_friends(userName=friend['UserName'])
                     # 如果是演示目的，把下面的方法改为print即可
                    itchat.send(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
                    time.sleep(.5)
                return 'send over'