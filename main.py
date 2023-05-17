# -*- coding: utf-8 -*-
from ImChang.linepy import *
from ImChang.akad import *
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from Naked.toolshed.shell import execute_js
from threading import Thread, active_count
import json,traceback,requests,re,ast,time,random,shutil
from random import randint
import gpt4free
from gpt4free import Provider
from googletrans import Translator
translator = Translator()

from getData import lottoFlex,lottoFlexAll,glotto,lottocheck,lotest,menuflex
login = json.loads(open('Data/token3.json','r').read())
setting = json.loads(open('Data/settings.json','r').read())

# if login["email"] == "":
#     try:
#         client = LINE(idOrAuthToken=login["token"])
#     except:
#         print("TOKEN EXPIRED");
# else:
#   client = LINE(login["email"],login["password"])
client = LINE(idOrAuthToken="Fr0kWcMFfzXzgW7WId07.ikNvhWs3jkc7oHDcaL9TvW.qBULkueR0tVNaMj51HU28NSesohZw9ZeJohSIFV0CeE=")
client.log("Auth Token : " + str(client.authToken))

admin = ["ued7545af3e0c0a348a18832777b9cee2","u0b499ce24e07b16ec12f8d0ba3ef8438"]

clPoll = OEPoll(client)
mid = client.profile.mid


def liff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {'on': ['P','CM'],'off': []}
    headers = {'X-Line-Access': client.authToken ,'X-Line-Application': client.server.APP_NAME,'X-Line-ChannelId': '1661040653','Content-Type': 'application/json'}
    requests.post(url, json=data, headers=headers)

def sendTemplate(to, data):
    drex = LiffChatContext(to)
    mobz = LiffContext(chat=drex)
    view = LiffViewRequest('1661040653-4knqkL7j', mobz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages": [data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendFlex(to, alt, flex):
    data = {"type": "flex", "altText": alt, "contents": flex}
    sendTemplate(to, data)

def sendFlexImage(to, imageUrl, animated=False):
    
    xnook = LiffChatContext(to)
    ynook = LiffContext(chat=xnook)
    view = LiffViewRequest('1661040653-4knqkL7j', ynook)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {
        'messages': [{
            'type': 'image',
            'originalContentUrl': imageUrl,
            'previewImageUrl': imageUrl,
            'animated': animated,
            'extension': 'jpg',
            'sentBy': {
                'label': '𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗔𝗡𝗖𝗘 𝗕𝗬 𝗡𝗢𝗢𝗞𝗗𝗘𝗩',
                'iconUrl': f'https://d96fylcqw0d34.cloudfront.net/nookassets/logo.png',
                'linkUrl': 'https://nook.com/'
            }
        }]
    }
    return requests.post(url, headers=headers, data=json.dumps(data))

def sendFlexVideo(to, videoUrl, thumbnail):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1661040653-4knqkL7j', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {
        'messages': [{
            'type': 'video',
            'originalContentUrl': "https://api.car2autobuy.com/vid/naka.mp4",
            'previewImageUrl': "https://d96fylcqw0d34.cloudfront.net/nookassets/logo.png",
            'sentBy': {
                'label': '𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗔𝗡𝗖𝗘 𝗕𝗬 𝗡𝗢𝗢𝗞𝗗𝗘𝗩',
                'iconUrl': f'https://d96fylcqw0d34.cloudfront.net/nookassets/logo.png',
                'linkUrl': 'https://nook.com/'
            }
        }]
    }
    return requests.post(url, headers=headers, data=json.dumps(data))




#LOTTOALLDATA = getDDD()
#print(LOTTOALLDATA['DD'],LOTTOALLDATA['SS'])
def STARTF():
    sentFtog = setting['groupLotto']
    for xx in sentFtog:
        sendFlex(xx, "หวย", lottoFlexAll())

def SENDFLEX(typelotto):
    sentFtog = setting['groupLotto']
    for xx in sentFtog:
        sendFlex(xx, "ประกาศผลหวย", lottoFlex(typelotto))
        
def SENDLATTE_THAIFLEX():
    sentFtog = setting['groupLotto']
    for xx in sentFtog:
        sendFlex(xx, "ประกาศผลหวย", glotto())

def Oup(op):
    try:
        if op.type == 0:
            return
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if setting["winvite"] == True:
                    if msg._from in admin:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = client.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                client.sendMessage(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                break
                            elif invite in setting["blacklist"]:
                                client.sendMessage(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                break                             
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    client.findAndAddContactsByMid(target)
                                    client.inviteIntoGroup(msg.to,[target])
                                    client.sendMessage(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                    setting["winvite"] = False
                                    break
                                except:
                                    try:
                                        client.findAndAddContactsByMid(invite)
                                        client.inviteIntoGroup(op.param1,[invite])
                                        setting["winvite"] = False
                                    except:
                                        client.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                        setting["winvite"] = False
                                        break

        if op.type == 26:
            msg = op.message
            nook = msg.text
            print(op)
            id = msg.id
            to = msg.to
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != client.getProfile().mid:to = sender
                    else:to = receiver
                if msg.toType == 1 or msg.toType == 2:to = msg.to
                if msg.contentType == 0:
                    if None == msg.text:return
                    cmd = msg.text.lower()
                    
                    if cmd == ".allowliff":
                        try:
                            liff()
                            client.sendFlexText(to,"Flex enabled.")
                        except:client.sendReplyMessage(id,to,"Click and allow url to enable flex\nline://app/1661040653-4knqkL7j")

                    if cmd== "@@@":
                        group = client.getGroup(msg.to)
                        midMembers = [contact.mid for contact in group.members]
                        midSelect = len(midMembers)//20
                        for mentionMembers in range(midSelect+1):
                            ret_ = "• L͎I͎N͎E͎B͎O͎T͎ •"
                            no = 0;dataMid = [];
                            for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                dataMid.append(dataMention.mid)
                                ret_ += "\n{}. @!\n".format(str(no))
                                no = (no+1)
                            ret_ += "\n\n「 รวม {} ท่าน 」\n𝙋𝙀𝙍𝙁𝙊𝙍𝙈𝘼𝙉𝘾𝙀 𝘽𝙔 𝙉𝙊𝙊𝙆𝘿𝙀𝙑".format(str(len(dataMid)))
                            client.sendMention(to, ret_, dataMid)

                    if cmd == "help":
                        contact = client.getContact(sender)
                        name = contact.displayName
                        result = {"type": "bubble", "size": "nano", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": f"{name.replace('.','').upper()}", "color": "#e00000", "weight": "bold"}, ], "backgroundColor": "#000000"} }
                        sendFlex(to, "LIST LOTTO MENU", result)

                    if cmd == "lotto":
                        sendFlex(to, "ประกาศผลหวย", lottoFlexAll())
                    
                    if cmd == "lothai":
                        sendFlex(to, "ประกาศผลหวย", glotto())
                        
                    if cmd == "tsk":
                        sendFlex(to, "ประกาศผลหวย", lotest())
                        
                    if cmd == "menu":
                        sendFlex(to, "เมนูผลหวย", menuflex("หวยรัฐบาล\nหวยออมสิน\nหวยธกส","หวยไทย"))
                    
                    if cmd == ".img":
                        imgurl = "https://tang.huaynaka.com/img/ng-104.e3060e54.png"
                        sendFlexImage(to, imgurl)

                    if cmd == ".vid":
                        vidURL = "https://api.car2autobuy.com/vid/naka.mp4"
                        imgURL = "https://tang.huaynaka.com/img/ng-104.e3060e54.png"
                        sendFlexVideo(to,vidURL,imgURL)
                        
                    if cmd == ".changyed":
                        midd = "u0b499ce24e07b16ec12f8d0ba3ef8438"
                        client.inviteIntoGroup(msg.to,[midd])

                    if cmd.startswith('.คอล'):
                        client.inviteIntoGroupCall(to,[uid.mid for uid in client.getGroup(to).members if uid.mid != client.getProfile().mid])
                        client.sendMessage(to,"เชิญเข้าร่วมการโทรสำเร็จ\n𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗔𝗡𝗖𝗘 𝗕𝗬 𝗡𝗢𝗢𝗞𝗗𝗘𝗩")
                        
                    if cmd.startswith('.call'):
                        if msg.toType == 2:
                            group = client.getGroup(to)
                            members = [mem.mid for mem in group.members]
                            client.acquireGroupCallRoute(to)
                            client.inviteIntoGroupCall(to, contactIds=members)
                            jmlh = int(100)
                            client.sendMessage(to, "โทรแบบกลุ่ม")
                            if jmlh <= 1000:
                                for x in range(jmlh):
                                    try:
                                        client.acquireGroupCallRoute(to)
                                        client.inviteIntoGroupCall(to, contactIds=members)
                                    except Exception as e:
                                        client.sendMessage(to,str(e))
                            else:
                                client.sendMessage(to,"เกินขีดจำกัด")
                    
                    if cmd == '⚠️':
                        if msg.toType == 2:
                            group = client.getGroup(to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//100
                            for a in range(k+1):
                                txt = ''
                                s=0
                                b=[]
                                for i in group.members[a*100 : (a+1)*100]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += '@Alin \n'
                                client.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                client.sendMessage(to, "จำนวนทั้งหมด {} ID\n𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗔𝗡𝗖𝗘 𝗕𝗬 𝗡𝗢𝗢𝗞𝗗𝗘𝗩".format(str(len(nama))))
                            
                    if cmd.startswith('.ตามมา '):
                        if msg.toType == 2:
                            midd = nook.replace(".ตามมา ","")
                            groupTarget = client.getGroup(midd)
                            mempoint = [contact.mid for contact in groupTarget.members]
                            k = len(mempoint)//100
                            for a in range(k+1):
                                for idpoint in groupTarget.members[a*100:(a+1)*100]:
                                    client.findAndAddContactsByMid(idpoint.mid)
                                    client.inviteIntoGroup(to,[idpoint.mid])
                                client.sendMessage(to, "จำนวนID เชิญมา {} ID\n𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗔𝗡𝗖𝗘 𝗕𝗬 𝗡𝗢𝗢𝗞𝗗𝗘𝗩".format(str(len(mempoint))))

                    if cmd.startswith("✅️ "):
                        if msg.toType == 2:
                            midd = nook.replace("✅️ ","")
                            client.findAndAddContactsByMid(midd)
                            client.inviteIntoGroup(to,[midd])
                            sendFlexImage(to,"https://d96fylcqw0d34.cloudfront.net/nookassets/logo.png")
                    
                    if cmd == "#ยกเชิญ":
                        if msg.toType == 2:
                            group = client.getGroup(to)
                            if group.invitee is None or group.invitee == []:
                                client.sendMessage(to, "ไม่มีสมาชิกค้างเชิญ")
                            else:
                                invitee = [contact.mid for contact in group.invitee]
                                for inv in invitee:
                                    client.cancelGroupInvitation(to, [inv])
                                    time.sleep(1)
                                client.sendMessage(to, "ยกเลิกสมาชิก 「 {} 」คน".format(str(len(invitee))))

                    if cmd.startswith("gbroadcast "):
                        sep = nook.split(" ")
                        txt = nook.replace(sep[0] + " ","")
                        groups = client.getGroupIdsJoined()
                        for group in groups:
                            try:client.sendMessage(group, "🎀  ประกาศ  🎀\n{}".format(str(txt)))
                            except:pass
                            time.sleep(3)
                        client.sendMessage(to, "สำเร็จ {} group".format(str(len(groups))))

                    if cmd.startswith("fbroadcast "):
                        sep = nook.split(" ")
                        txt = nook.replace(sep[0] + " ","")
                        groups = client.getAllContactIds()
                        for group in groups:
                            try:client.sendMessage(group, "🎀  ประกาศ  🎀\n{}".format(str(txt)))
                            except:pass
                            time.sleep(3)
                        client.sendMessage(to, "สำเร็จ {} friend".format(str(len(groups))))
                    
                    if cmd.startswith(".join "):
                        data = cmd.split("join ")[1]
                        if data == "on":
                            if setting["join"]:client.sendMessage(to,"already enabled.")
                            else:setting["join"] = True
                            with open('Data/settings.json', 'w') as fp:
                                json.dump(setting, fp, sort_keys=True, indent=4)
                            client.sendMessage(to,"join enabled.")
                        if data == "off":
                            if setting["join"] == False:client.sendMessage(to,"already disabled.")
                            else:setting["join"] = False
                            with open('Data/settings.json', 'w') as fp:
                                json.dump(setting, fp, sort_keys=True, indent=4)
                            client.sendMessage(to,"already disabled.") 

                    if cmd.startswith(".ticket "):
                        data = cmd.split("ticket ")[1]
                        if data == "on":
                            if setting["ticket"]:client.sendMessage(to,"already enabled.")
                            else:setting["ticket"] = True
                            with open('Data/settings.json', 'w') as fp:
                                json.dump(setting, fp, sort_keys=True, indent=4)
                            client.sendMessage(to,"Join ticket enabled.")
                        if data == "off":
                            if setting["ticket"] == False:client.sendMessage(to,"Join ticket disabled.")
                            else:setting["ticket"] = False
                            with open('Data/settings.json', 'w') as fp:
                                json.dump(setting, fp, sort_keys=True, indent=4)
                            client.sendMessage(to,"already disabled.")

                    if nook.startswith("flex: "):
                        datatypelotto = nook.strip().split("flex: ")[1]
                        print(datatypelotto)
                        if datatypelotto == "LATTE_THAI":
                           SENDLATTE_THAIFLEX() 
                        else:
                           SENDFLEX(datatypelotto)
                    
                    mlottox = re.search(r"\d{6}",cmd)
                    if mlottox:
                        lottoXS = lottocheck(mlottox.group())
                        contact = client.getContact(sender)
                        #print(contact)
                        if lottoXS:
                            client.sendMessage(to,"ยินดีกับ "+contact.displayName+" \nถูกหวย "+lottoXS[0]+" เลข "+lottoXS[1]+"\n")
                        else:
                            client.sendMessage(to,"ไม่ถูก เอาใหม่นะ "+contact.displayName)
                            
                    
                    if cmd.startswith(".bn"):
                        msgx = cmd.replace(".bn","")
                        contact = client.getContact(sender)
                        inresse = translator.translate(msgx, dest='en')
                        response = gpt4free.Completion.create(Provider.You, prompt=inresse)
                        resse = translator.translate(response, dest='th')
                        client.sendMessage(to, "รอสักครู่..."+"\n"+contact.displayName)
                        time.sleep(3)
                        client.sendMessage(to, resse+"\n"+contact.displayName)
                        
    except Exception as error:
        print(error)

while True:
    try:
        ops = clPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clPoll.setRevision(op.revision)
                t1 = Thread(target=Oup(op,))
                t1.start()
                t1.join()
    except Exception as error:
        client.log("「 ERROR 」\n{}".format(str(error)))
        traceback.print_tb(error.__traceback__)