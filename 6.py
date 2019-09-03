#==========================================#
# Arif Suleng Bots #
#==========================================#
# Verci 1Sb 5Bot 1Ajs #
#==========================================#
# Jangan Merubah Apapun Yang Ada Didalam SC ini
# Apa bila Tetap Dilanggar & Terjadi Eror atau Rusak
# Resiko Ditanggung Penumpang Terimakasih
# Gunakan Bot Dengan Bijak Jangan Sombong
# Ingat Diatas Langit Masih Ada Langit
#==========================================#

#==========================================#
import suleng
from suleng import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl


#eowyn.harnoor@lnsilver.ccom
#sodron03
#franko.addis@lnsilver.com
#sodron03
#golden.brandi@lnsilver.com
#sodron03
#antoni.hank@lnsilver.ccom
#sodron03
#evonna.brissia@lnsilver.com
#sodron03
#drayvin.dravin@lnsilver.com
#sodron03

# Kepala ===============================
cl = LineClient("andrie02bre@gmail.com","sodron01")
cl.log("Auth Token : " + str(cl.authToken))
print("\nSukses Login { SB } Suleng Bots\n")
print("\nSiap Login Bots { 1 } Berikutnya\n")
lineProfile = cl.getProfile()
lineSettings = cl.getSettings()
mid = cl.getProfile().mid
responsename = cl.getProfile().displayName
# Selesai ===============================
k1 = LineClient("eowyn.harnoor@lnsilver.com","sodron03")
k1.log("Auth Token : " + str(k1.authToken))
print("\nSukses Login { BOT 1 } Suleng Bots\n")
print("\nSiap Login Bots { 2 } Berikutnya\n")
lineProfile = k1.getProfile()
lineSettings = k1.getSettings()
Amid = k1.getProfile().mid
responsename1 = k1.getProfile().displayName
# Selesai ===============================
k2 = LineClient("franko.addis@lnsilver.com","sodron03")
k2.log("Auth Token : " + str(k2.authToken))
print("\nSukses Login { BOT 2 } Suleng Bots\n")
print("\nSiap Login Bots { 3 } Berikutnya\n")
lineProfile = k2.getProfile()
lineSettings = k2.getSettings()
Bmid = k2.getProfile().mid
responsename2 = k2.getProfile().displayName
# Selesai ===============================
k3 = LineClient("golden.brandi@lnsilver.com","sodron03")
k3.log("Auth Token : " + str(k3.authToken))
print("\nSukses Login { BOT 3 } Suleng Bots\n")
print("\nSiap Login Bots { 4 } Berikutnya\n")
lineProfile = k3.getProfile()
lineSettings = k3.getSettings()
Cmid = k3.getProfile().mid
responsename3 = k3.getProfile().displayName
# Selesai ===============================
k4 = LineClient("antoni.hank@lnsilver.com","sodron03")
k4.log("Auth Token : " + str(k4.authToken))
print("\nSukses Login { BOT 4 } Suleng Bots\n")
print("\nSiap Login Bots { 5 } Berikutnya\n")
lineProfile = k4.getProfile()
lineSettings = k4.getSettings()
Dmid = k4.getProfile().mid
responsename4 = k4.getProfile().displayName
# Selesai ===============================
k5 = LineClient("evonna.brissia@lnsilver.com","sodron03")
k5.log("Auth Token : " + str(k5.authToken))
print("\nSukses Login { BOT 5 } Suleng Bots\n")
lineProfile = k5.getProfile()
lineSettings = k5.getSettings()
Emid = k5.getProfile().mid
responsename5 = k5.getProfile().displayName
# Selesai ===============================
sw = LineClient("drayvin.dravin@lnsilver.com","sodron03")
sw.log("Auth Token : " + str(sw.authToken))
print("\nSukses Login { Ajs 1 } Suleng Bots\n")
lineProfile = sw.getProfile()
lineSettings = sw.getSettings()
Zmid = sw.getProfile().mid
responsename6 = sw.getProfile().displayName
# Selesai ===============================

print ("==Selesai==Selesai==Selesai==Selesai==")
print ("=================================")
print ("All Bots Suleng Login Sukses")
print ("Selamat Menggunakan Bots Suleng")
print ("Creator Arif Suleng Bots")
print ("=================================")
print ("==Selesai==Selesai==Selesai==Selesai==")

poll = LinePoll(cl)
call = cl
creator = ["ue34fccd62846170bbe9369bf8895ee55"]
owner = ["ue10fa4211368ea5b7dda07765983fda6"]
admin = ["ue10fa4211368ea5b7dda07765983fda6"]
staff = ["ue10fa4211368ea5b7dda07765983fda6"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,k1,k2,k3,k4,k5]
ABC = [k1,k2,k3,k4,k5]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectcancel = []
protectname = []
welcome = []
targets = []
protectname = []
prohibitedWords = ['Asu', 'Jancok', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []

responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName

settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "changePicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "suleng":{},
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "leaveOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "mention":"Selamat Menginceng Semoga Anda Gelem Melu Chat",
    "Respontag":"Tag Nama Saya Se x Lg Anda Dapat Hadiah 1 Gelas Cantik Dari Para Admin",
    "welcome":"┏━━━━━━━━━━━━━━━━━━━━━━━━━\n┃ Selamat Datang Di Group Kami\n┃Jangan Lupa Cek Note Ya..???\n┃Jika Ada Kesulitan Hubungi Admin\n┃Apabila Sakit Berlanjut Hubungi Dokter \n┗━━━━━━━━━━━━━━━━━━━━━━━━━",
    "leave":"┏━━━━━━━━━━━━━━━━━━━━━━━━━━\n┃Selamat Jalan Jurangan...???\n┃Hati Hati Di Jalan Ya..???\n┃Semoga Lain Waktu Jumpa Lagi\n┗━━━━━━━━━━━━━━━━━━━━━━━━━",
    "comment":"🔰Auto like By Arif Suleng Bots🔰",
    "comment1":"🔰Auto like By Arif Suleng Bots🔰",
    "message":"🔰🔰Thank For Add Me Guys🔰🔰\n\n\n🔞Open Order Segala Macam Bot🔞\n\n🎯SB Unly Biasa\n🎯SB Unly Pro\n🎯SB Unly Template\n\n🔰Jenis Bot Protect Group🔰\n\n💥1Sb 3bot 2Ghost 1Ajs\n💥1Sb 5Bot 2Ghost 1Ajs\n💥1Sb 6Bot 2Ghost 2Ajs\n💥1Sb 5Bot 5Ghost 2Ajs\n💥1Sb 13Bot 3Ghost 2Ajs\n💥1Sb 5bot 1Ajs\n💥1Sb 7bot 1Ajs\n💥1Sb 8bot 2Ajs\n💥1Sb 10Bot 2Ajs\n💥1Sb 12Bot 2Ajs\n\n\n🔰SC Bisa Request Minat Hubungi\n\n🔰Creator https://line.me/ti/p/~raccell19🔰\n\nTerima Kasih Semoga Saya Bisa Menjadi Teman Yang Baik Untuk Anda"
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "ghost":[],
    "protect":[],
    "protectcancel":[],
    "protectname":[],
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
arifProfile = cl.getProfile()
myProfile["displayName"] = arifProfile.displayName
myProfile["statusMessage"] = arifProfile.statusMessage
myProfile["pictureStatus"] = arifProfile.pictureStatus
myProfile["changPicture"] = arifProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ Suleng Bots ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        cl.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User {} \nHolla ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "┏━━━━━━━━━━━━━━━━━━━━━━━━━\n┃  Team Arif Suleng Bots\n┗━━━━━━━━━━━━━━━━━━━━━━━━━\n  Welcome Guys  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\n\nDi "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "┏━━━━━━━━━━━━━━━━━━━━━━━━━\n┃  Team Arif Suleng Bots\n┗━━━━━━━━━━━━━━━━━━━━━━━━━\n  Leave / Kabur  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Suleng Bots\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "┏━━━━━━━━━━━━━━━━━\n┃ Jumlah Member {} \n┗━━━━━━━━━━━━━━━━━\n┏━━━━━━━━━━━━━━━━━\n┃ [ Team Arif Suleng Bots ]\n┗━━━━━━━━━━━━━━━━━\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┃ [ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Hallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "┏━━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🆎┫ 🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┃🆎┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┃🆎┣━━━━━━🍁┫ Menu ┣🍁━━━━━━" + "\n" + \
                  "┣🆎┫ " + key + "Cctv「on/off」\n" + \
				  "┣🆎┫ " + key + "Contact Admin\n" + \
                  "┣🆎┫ " + key + "Contact Bot\n" + \
				  "┣🆎┫ " + key + "Creator\n" + \
				  "┣🆎┫ " + key + "Cyduk\n" + \
				  "┣🆎┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🆎┃  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🆎┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
				  "┣🆎┫ " + key + "Help 1\n" + \
				  "┣🆎┫ " + key + "Help 2\n" + \
                  "┣🆎┫ " + key + "Help 3\n" + \
				  "┣🆎┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🆎┃  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🆎┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🆎┫ " + key + "Stafflist\n" + \
                  "┣🆎┫ " + key + "Admin\n" + \
				  "┣🆎┫ " + key + "Staff\n" + \
				  "┃🆎┣━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🆎┫http://line.me/ti/p/~raccell19" + "\n" + \
                  "┗━━┫ CREATOR: ©Arif Suleng™┣━━━"
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "┏━━━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┃🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃   🎯🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫ " + key + "Csider\n" + \
                  "┣🔇┫ " + key + "Cspam\n" + \
                  "┣🔇┫ " + key + "Sider on\off\n" + \
                  "┣🔇┫ " + key + "Cpesan\n" + \
                  "┣🔇┫ " + key + "Crespon\n" + \
                  "┣🔇┫ " + key + "Cwelcome\n" + \
                  "┣🔇┫ " + key + "Cleave\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃   🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫ " + key + "Ssider「Text」\n" + \
                  "┣🔇┫ " + key + "Sspam「Text」\n" + \
                  "┣🔇┫ " + key + "Spesan「Text」\n" + \
                  "┣🔇┫ " + key + "Srespon「Text」\n" + \
                  "┣🔇┫ " + key + "Swelcome「Text」\n" + \
                  "┣🔇┫ " + key + "Sleave「Text」\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫ " + key + "Myname「Nama」\n" + \
                  "┣🔇┫ " + key + "Bot1name「Nama」\n" + \
                  "┣🔇┫ " + key + "Bot2name「Nama」\n" + \
                  "┣🔇┫ " + key + "Bot3name「Nama」\n" + \
                  "┣🔇┫ " + key + "Bot4name「Nama」\n" + \
                  "┣🔇┫ " + key + "Bot5name「Nama」\n" + \
                  "┣🔇┫ " + key + "Jname「Nama」\n" + \
				  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫ " + key + "Bot1up「foto」\n" + \
                  "┣🔇┫ " + key + "Bot2up「foto」\n" + \
                  "┣🔇┫ " + key + "Bot3up「foto」\n" + \
                  "┣🔇┫ " + key + "Bot4up「foto」\n" + \
                  "┣🔇┫ " + key + "Bot5up「foto」\n" + \
                  "┣🔇┫ " + key + "Jsup「foto」\n" + \
				  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫ " + key + "Gift「Mid」「Jumlah」\n" + \
                  "┣🔇┫ " + key + "Spam「Mid」「Jumlah」\n" + \
				  "┣🔇┫ " + key + "Spamtag「jumlah」\n" + \
                  "┣🔇┫ " + key + "Spamtag「@」\n" + \
                  "┣🔇┫ " + key + "Spamcall「jumlah」\n" + \
                  "┣🔇┫ " + key + "Spamcall\n" + \
				  "┣🔇┫ " + key + "Updatefoto\n" + \
                  "┣🔇┫ " + key + "Updategrup\n" + \
                  "┣🔇┫ " + key + "Updatebot\n" + \
                  "┣🔇┫ " + key + "Broadcast:「Text」\n" + \
                  "┣🔇┫ " + key + "Setkey「New Key」\n" + \
                  "┣🔇┫ " + key + "Mykey\n" + \
                  "┣🔇┫ " + key + "Resetkey\n" + \
				  "┣🔇┫ " + key + "Self「on/off」\n" + \
                  "┣🔇┫ " + key + "Remove chat\n" + \
				  "┣🔇┫ " + key + "Leave「Namagrup」\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫ " + key + "Blc\n" + \
                  "┣🔇┫ " + key + "Ban:on\n" + \
                  "┣🔇┫ " + key + "Unban:on\n" + \
                  "┣🔇┫ " + key + "Ban「@」\n" + \
                  "┣🔇┫ " + key + "Unban「@」\n" + \
                  "┣🔇┫ " + key + "Talkban「@」\n" + \
                  "┣🔇┫ " + key + "Untalkban「@」\n" + \
                  "┣🔇┫ " + key + "Talkban on\n" + \
                  "┣🔇┫ " + key + "Untalkban on\n" + \
                  "┣🔇┫ " + key + "Banlist\n" + \
                  "┣🔇┫ " + key + "Talkbanlist\n" + \
                  "┣🔇┫ " + key + "Clearban\n" + \
                  "┣🔇┫ " + key + "Refresh\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┃  🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔇┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔇┫  🆔 LiNE : raccell19" + "\n" + \
                  "┗🔇┫ CREATOR: ©Arif Suleng™  ┣━━━"
    return helpMessage1
	
def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "┏━━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔌┫ 🔕🔕🔕 Suleng Bots 🔕🔕🔕 " + "\n" + \
                  "┃🔌┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┃🔌┣━━━━━🎸┫ Admin ┣🎸━━━━━━" + "\n" + \
                  "┣🔌┫ " + key + "Admin on\n" + \
                  "┣🔌┫ " + key + "Adminexpl on\n" + \
                  "┣🔌┫ " + key + "Staff on\n" + \
                  "┣🔌┫ " + key + "Staffexpl on\n" + \
                  "┣🔌┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔌┃ 🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔌┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔌┫ " + key + "Addadmin「@」\n" + \
                  "┣🔌┫ " + key + "Delladmin「@」\n" + \
                  "┣🔌┫ " + key + "Addstaff「@」\n" + \
                  "┣🔌┫ " + key + "Dellstaff「@」\n" + \
                  "┣🔌┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔌┃   🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🔌┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔌┫ " + key + "Bot on「@」\n" + \
                  "┣🔌┫ " + key + "Botexpl on「@」\n" + \
                  "┣🔌┫ " + key + "Refresh / Fresh\n" + \
                  "┃🔌┣━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🔌┫http://line.me/ti/p/~raccell19" + "\n" + \
                  "┗━━┫ CREATOR: ©Arif Suleng™┣━━━"
    return helpMessage2
    	
def help3():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "┏━━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┫   🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┃🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┫ " + key + "Autoadd「on/off」\n" + \
				  "┣🎯┫ " + key + "Autojoin「on/off」\n" + \
				  "┣🎯┫ " + key + "Autoleave「on/off」\n" + \
				  "┣🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
				  "┣🎯┫ " + key + "Contact「on/off」\n" + \
				  "┣🎯┫ " + key + "Jointicket「on/off」\n" + \
				  "┣🎯┫ " + key + "Respon「on/off」\n" + \
                  "┣🎯┫ " + key + "Respongift「on/off」\n" + \
                  "┣🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣🎯┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
				  "┣🎯┫ " + key + "Sticker「on/off」\n" + \
				  "┣🎯┫ " + key + "Unsend「on/off」\n" + \
                  "┣🎯┫ " + key + "Welcome「on/off」\n" + \
                  "┣🎯┫ " + key + "Addimg\n" + \
				  "┣🎯┫ " + key + "Dellimg\n" + \
                  "┣🎯┫ " + key + "Listimg\n" + \
                  "┃🎯┣━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣🎯┫http://line.me/ti/p/~raccell19" + "\n" + \
                  "┗━━┫ CREATOR: ©Arif Suleng™┣━━━"
    return helpMessage3
    
def help4():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "┏━━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃    🎯🔰🎯 PROTECTION 🎯🔰🎯 " + "\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
				  "┣📲┃ " + key + "In\n" + \
				  "┣📲┃ " + key + "Out\n" + \
				  "┣📲┃ " + key + "Js「on/off」\n" + \
				  "┣📲┃ " + key + "Stay\n" + \
				  "┣📲┃ " + key + "Ajs in\n" + \
				  "┣📲┃ " + key + "Ajs bye\n" + \
                  "┣📲┃ " + key + "Notag「on/off」\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃    🎯🔰🎯 Ngratain 🎯🔰🎯 " + "\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃ " + key + "Bubar\n" + \
                  "┣📲┃ " + key + "Suleng\n" + \
                  "┣📲┃ " + key + "Kicker @\n" + \
                  "┣📲┃ " + key + "Vc @\n" + \
                  "┣📲┃ " + key + "Bl\n" + \
                  "┣📲┃ " + key + "Gas\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃ " + key + "Proall「on/off」\n" + \
                  "┣📲┃ " + key + "Protect「on/off」\n" + \
                  "┣📲┃ " + key + "Protectkick「on/off」\n" + \
                  "┣📲┃ " + key + "Procancel「on/off」\n" + \
                  "┣📲┃ " + key + "Proinvite「on/off」\n" + \
				  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣📲┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣📲┃  http://line.me/ti/p/~raccell19" + "\n" + \
                  "┗━━┫ CREATOR: ©Arif Suleng™┣━━━"
    return helpMessage4
	
def help5():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "┏━━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣💢┫ 💢💢💢 Suleng Bots 💢💢💢 " + "\n" + \
                  "┃💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣💢┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣💢┫ " + key + "About\n" + \
				  "┣💢┫ " + key + "Bye Arif\n" + \
                  "┣💢┫ " + key + "Bye protect\n" + \
				  "┣💢┫ " + key + "Curl\n" + \
				  "┣💢┫ " + key + "Ourl\n" + \
				  "┣💢┫ " + key + "Ginfo\n" + \
				  "┣💢┫ " + key + "Glist\n" + \
				  "┣💢┫ " + key + "Info 「@」\n" + \
				  "┣💢┫ " + key + "Infogrup「angka」\n" + \
                  "┣💢┫ " + key + "Infomem「angka」\n" + \
                  "┣💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣💢┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
				  "┣💢┫ " + key + "Invitebot\n" + \
				  "┣💢┫ " + key + "「@」Kick\n" + \
				  "┣💢┫ " + key + "「@」Kick1\n" + \
				  "┣💢┫ " + key + "Me\n" + \
                  "┣💢┫ " + key + "Mid「@」\n" + \
				  "┣💢┫ " + key + "Mybackup\n" + \
				  "┣💢┫ " + key + "Mybot\n" + \
				  "┣💢┫ " + key + "Mycopy「@」\n" + \
                  "┣💢┫ " + key + "Mymid\n" + \
                  "┣💢┫ " + key + "Get mid @\n" + \
                  "┣💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣??┃    🎯🔰🎯 Suleng Bots 🎯🔰🎯 " + "\n" + \
                  "┣💢┣━━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
				  "┣💢┫ " + key + "Open\n" + \
				  "┣💢┫ " + key + "Reject\n" + \
				  "┣💢┫ " + key + "Respon\n" + \
				  "┣💢┫ " + key + "Restart\n" + \
				  "┣💢┫ " + key + "Runtime\n" + \
				  "┣💢┫ " + key + "Sider「PREMI」\n" + \
				  "┣💢┫ " + key + "Speed/Sp\n" + \
                  "┣💢┫ " + key + "Sprespon\n" + \
				  "┣💢┫ " + key + "Stealname「@」\n" + \
                  "┣💢┫ " + key + "Stealbio「@」\n" + \
                  "┣💢┫ " + key + "Stealcover「@」\n" + \
				  "┣💢┫ " + key + "Stealpicture「@」\n" + \
                  "┣💢┫ " + key + "Stealvideoprofile「@」\n" + \
                  "┣💢┫ " + key + "Absen \ Tagall\n" + \
                  "┣💢┫ " + key + "Url grup\n" + \
                  "┃💢┣━━━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣💢┫http://line.me/ti/p/~raccell19" + "\n" + \
                  "┗━━┫ CREATOR: ©Arif Suleng™┣━━━"
    return helpMessage5

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protect["pqr"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            cl.updateGroup(X)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = k1.reissueGroupTicket(op.param1)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                #k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k1.updateGroup(X)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = k2.reissueGroupTicket(op.param1)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    #k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k2.updateGroup(X)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = k3.reissueGroupTicket(op.param1)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        #k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k3.updateGroup(X)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = k4.reissueGroupTicket(op.param1)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            #k5.kickoutFromGroup(op.param1,[op.param2])
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                            k4.updateGroup(X)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = k5.reissueGroupTicket(op.param1)
                                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                #k6.kickoutFromGroup(op.param1,[op.param2])
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                k1.updateGroup(X)
                                    except:
                                        pass
                      
        if op.type == 11:
            if op.param1 in warmode:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            wait["blacklist"][op.param2] = True
                            try:k1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                            	try:k2.kickoutFromGroup(op.param1,[op.param2])
                            	except:
                            	    try:k3.kickoutFromGroup(op.param1,[op.param2])
                            	    except:
                            	        try:k4.kickoutFromGroup(op.param1,[op.param2])
                            	        except:
                            	            try:k5.kickoutFromGroup(op.param1,[op.param2])
                            	            except:pass
                            warmode.remove(op.param1)
                except:pass
       
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                   try:k1.kickoutFromGroup(op.param1,[op.param2])
                   except:
                   	try:k2.kickoutFromGroup(op.param1,[op.param2])
                   	except:
                   	    try:k3.kickoutFromGroup(op.param1,[op.param2])
                   	    except:
                               try:k4.kickoutFromGroup(op.param1,[op.param2])
                               except:
                                    try:k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                   	                 try:cl.reissueGroupTicket(op.param1);X = cl.getGroup(op.param1);X.preventedJoinByTicket = True;Ticket = cl.reissueGroupTicket(op.param1);sw.acceptGroupInvitationByTicket(op.param1,Ticket);sw.kickoutFromGroup(op.param1,[op.param2])
                   	                 except:pass
                   cl.reissueGroupTicket(op.param1)
                   X = cl.getGroup(op.param1)
                   X.preventedJoinByTicket = True
                   cl.updateGroup(X)
                   warmode.append(op.param1)
                else:
                   pass

#========================== PROTECTUPDATEGROUP                          
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Sorry anda bukan admin kami\nSelamat tinggal " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Terimakasih Telah Invite Saya Ssemoga Saya Bisa Jadi Teman Baik Untuk Semua Yang Ada Disini Amiin " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"I'm coming " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"I'm coming " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)                        
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)                                             
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)                        
                        k2.leaveGroup(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)                       
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)                       
                        k3.leaveGroup(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)                      
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k4.acceptGroupInvitation(op.param1)
                        ginfo = k4.getGroup(op.param1)                        
                        k4.leaveGroup(op.param1)
                    else:
                        k4.acceptGroupInvitation(op.param1)                        
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k5.acceptGroupInvitation(op.param1)
                        ginfo = k5.getGroup(op.param1)                        
                        k5.leaveGroup(op.param1)
                    else:
                        k5.acceptGroupInvitation(op.param1)

                return

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])


        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
#____________________________________________________________________
        if op.type == 13:
            if op.param1 in protect['pinv']:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            group = k1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                k1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                               group = k2.getGroup(op.param1)
                               gMembMids = [contact.mid for contact in group.invitee]
                               for _mid in gMembMids:
                                   random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                   k2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                               try:
                                   group = k3.getGroup(op.param1)
                                   gMembMids = [contact.mid for contact in group.invitee]
                                   for _mid in gMembMids:
                                       random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                       k3.kickoutFromGroup(op.param1,[op.param2])
                               except:
                                   try:
                                      group = k4.getGroup(op.param1)
                                      gMembMids = [contact.mid for contact in group.invitee]
                                      for _mid in gMembMids:
                                          random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                          k4.kickoutFromGroup(op.param1,[op.param2])
                                   except:
                                      try:
                                          group = k5.getGroup(op.param1)
                                          gMembMids = [contact.mid for contact in group.invitee]
                                          for _mid in gMembMids:
                                              random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                              k5.kickoutFromGroup(op.param1,[op.param2])
                                      except:
                                          pass
                                    
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k1.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k2.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k3.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                    	k4.cancleGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                        	k5.cancleGroupInvitation(op.param1,[op.param2])
                                        except:
                                            pass

                return
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                           pass
                           
                return
        if op.type == 32:
            if op.param1 in protectname:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                           pass
                           
                return
#__________________________________ 
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	k4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	k5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass

                return
#____________________________________________________________________               
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	k4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	k5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass

                return
#________________________________                                            
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        #cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        k1.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            #cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            k2.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                #cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                k3.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                    #cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    k4.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        #cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        k5.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = k1.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k1.updateGroup(G)
                                            Ticket = k1.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            G = k2.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            k2.updateGroup(G)
                                            Ticket = k2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k5.kickoutFromGroup(op.param1,[op.param2])

                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                        #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        k2.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                            #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            k3.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                                #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                k4.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                    #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    k5.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                        #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            cl.updateGroup(G)
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                        #k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        k1.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                            #k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            k3.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                                #k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                k4.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                    #k2.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    k5.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                        #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            cl.updateGroup(G)
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                        #k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        k2.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                            #k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            k1.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                                #k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                k4.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                    #k3.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    k5.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                        #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            cl.updateGroup(G)
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                        #k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        k2.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                            #k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            k3.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                                #k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                k1.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k4.acceptGroupInvitation(op.param1)
                                    #k4.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    k5.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k4.acceptGroupInvitation(op.param1)
                                        #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            cl.updateGroup(G)
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                        #k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                        k2.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                            #k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                            k3.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                                #k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                k4.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    k5.acceptGroupInvitation(op.param1)
                                    #k5.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                    k1.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        k5.acceptGroupInvitation(op.param1)
                                        #k1.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = cl.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            cl.updateGroup(G)
                                            Ticket = cl.reissueGroupTicket(op.param1)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
#____________________________________________________________________
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
                        k1.sendMessage(op.param1, wait["message"])
                        k2.sendMessage(op.param1, wait["message"])
                        k3.sendMessage(op.param1, wait["message"])
                        k4.sendMessage(op.param1, wait["message"])
                        k5.sendMessage(op.param1, wait["message"])
                        sw.sendMessage(op.param1, wait["message"])

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in settings['Protectname']:
                    try:
                        G = random.choice(ABC).getGroup(op.param1)
                    except:
                        pass
                    G.name = settings['protectname'][op.param1]
                    try:
                        random.choice(ABC).updateGroup(G)
                    except:
                        pass
                    if op.param2 in settings["admin"] or op.param2 in Bots:
                    	pass
                    else:
                        try:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).sendMessage(op.param1, "ãã€[Protect name]ãã†ã§ã™ã‹(ï½€ãƒ»Ï‰ãƒ»Â´)")
                        except:
                            pass
        if op.param3 == "1":
            if op.param1 in settings["protectname"]:
                group = cl.getGroup(op.param1)
                try:
                    group.name = settings["protectname"][op.param1]
                    cl.updateGroup(group)
                    cl.sendMessage(op.param1, "Nama Group Di Kunci Guys...???")
                    settings["blacklist"][op.param2] = True
                except Exception as e:
                    print(e)
                    pass

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "Gambar Di Hapus\nPengirim : "
                                ret_ = "Nama Group: {}".format(str(ginfo.name))
                                ret_ += "\Waktu Mengirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nTeam Arif Suleng Bots"
                                ret_ += "\nCreator:  line.me/ti/p/~raccell19" 
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "Pesan Dihapus\n"
                                ret_ += "Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\nNama Group : {}".format(str(ginfo.name))
                                ret_ += "\nWaktu Mengirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nIsi Pesanya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\nTeam Arif Suleng Bots"
                                ret_ += "\nCreator:  line.me/ti/p/~raccell19" 
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "Sticker Dihapus\n"
                                ret_ += "Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\nNama Group : {}".format(str(ginfo.name))
                                ret_ += "\nWaktu Mengirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\nTeam Arif Suleng Bots"
                                ret_ += "\nCreator:  line.me/ti/p/~raccell19" 
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.coice(ABC).findAndAddContactsByMid(op.param1,[Zmid])
                                random.coice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.coice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass

        if op.type == 32:
            if op.param3 in Zmid:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          k1.kickoutFromGroup(op.param1,[op.param2])
                          #k1.kickoutFromGroup(op.param1,[op.param2])
                          k1.inviteIntoGroup(op.param1,[Zmid])
                          cl.sendMessage(op.param1, "Itu Anti JS Jangan Di Cancel Cipok Sisan Kapok")
                  except:
                      try:
                          if op.param3 not in wait["blacklist"]:
                              k2.kickoutFromGroup(op.param1,[op.param2])
                              #k2.kickoutFromGroup(op.param1,[op.param2])
                              k2.inviteIntoGroup(op.param1,[Zmid])
                              cl.sendMessage(op.param1, "Itu Anti JS Jangan Di Cancel Cipok Sisan Kapok")
                      except:
                          try:
                              if op.param3 not in wait["blacklist"]:
                                  k3.kickoutFromGroup(op.param1,[op.param2])
                                  #k3.kickoutFromGroup(op.param1,[op.param2])
                                  k3.inviteIntoGroup(op.param1,[Zmid])
                                  cl.sendMessage(op.param1, "Itu Anti JS Jangan Di Cancel Cipok Sisan Kapok")
                          except:
                              try:
                                  if op.param3 not in wait["blacklist"]:
                                      k4.kickoutFromGroup(op.param1,[op.param2])
                                      #k4.kickoutFromGroup(op.param1,[op.param2])
                                      k4.inviteIntoGroup(op.param1,[Zmid])
                                      cl.sendMessage(op.param1, "Itu Anti JS Jangan Di Cancel Cipok Sisan Kapok")
                              except:
                                  try:
                                      if op.param3 not in wait["blacklist"]:
                                          k5.kickoutFromGroup(op.param1,[op.param2])
                                          #k5.kickoutFromGroup(op.param1,[op.param2])
                                          k5.inviteIntoGroup(op.param1,[Zmid])
                                          cl.sendMessage(op.param1, "Itu Anti JS Jangan Di Cancel Cipok Sisan Kapok")
                                  except:
                                      pass

              return
#___________________________________________________________________
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        random.coice(ABC).findAndAddContactsByMid(op.param3)                       
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    #random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    
            if op.param1 in protect["antijs"]:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                        k5.inviteIntoGroup(op.param1,[staff])
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        #cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        #cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        #cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            except:
                pass

        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                if receiver in temp_flood:
                    if temp_flood[receiver]["expire"] == True:
                        if cmd == "open" and sender == mid:
                            temp_flood[receiver]["expire"] = False
                            temp_flood[receiver]["time"] = time.time()
                            cl.sendMessage(to, "Bot Sudah Kembali Aktif Juragan.....???")
                        return
                    elif time.time() - temp_flood[receiver]["time"] <= 5:
                        temp_flood[receiver]["flood"] += 1
                        if temp_flood[receiver]["flood"] >= 100:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            ret_ = "Spam Terdeteksi\nBot Akan Silent Selama 30 Tahun\nSegera Ketik {}Open Untuk Mengaktifkan Kembali.".format(setKey)
                            cl.sendMessage(to, str(ret_))
                            cl.sendMessage(to, "Open")
                    else:
                         temp_flood[receiver]["flood"] = 0
                         temp_flood[receiver]["time"] = time.time()
                else:
                    temp_flood[receiver] = {
    	                "time": time.time(),
    	                "flood": 0,
    	                "expire": False
                    }
#____________________________________________________________________                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)

            if msg.contentType == 16:
                       url = msg.contentMetadata["postEndUrl"]
                       cl.like(url[25:58], url[66:], likeType=1001)
                       k1.like(url[25:58], url[66:], likeType=1001)
                       k2.like(url[25:58], url[66:], likeType=1001)
                       cl.comment(url[25:58], url[66:], wait["comment"])
                       k1.comment(url[25:58], url[66:], wait["comment"])
                       k2.comment(url[25:58], url[66:], wait["comment"])                 
        
                                                        
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              k1.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  k2.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	k3.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      try:
                                  	    k4.kickoutFromGroup(msg.to, [msg._from])
                                      except:
                                          try:
                                  	        k5.kickoutFromGroup(msg.to, [msg._from])
                                          except:
                                              pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention1(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "No tag me....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots&media
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in Talkban")
#UPDATE FOTO
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")

               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Sukses Mengganti Nama Group")

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["changePicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["chanhePicture"] = False
                     cl.updateProfilePicture(msg.to, path)
                     cl.sendMessage(msg.to, "Sukses Mengganti Nama Group")

               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Amid in Setmain["RAfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["Bfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["RAfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["RAfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["RAfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")
                            
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = k1.downloadObjectMsg(msg_id)
                     path2 = k2.downloadObjectMsg(msg_id)
                     path3 = k3.downloadObjectMsg(msg_id)
                     path4 = k4.downloadObjectMsg(msg_id)
                     path5 = k5.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     k1.updateProfilePicture(path1)
                     k1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k2.updateProfilePicture(path1)
                     k2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k3.updateProfilePicture(path3)
                     k3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k4.updateProfilePicture(path4)
                     k4.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     k5.updateProfilePicture(path5)
                     k5.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path6)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Bot Telah Diactifkan🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Bot Dinonactifkan🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━")


                        elif cmd == 'vp':
                        	if msg._from in owner or msg._from in admin:
                                 me = cl.getContact(mid)
                                 cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                            
                        elif cmd == "help1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage1 = help1()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = help2()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage3 = help3()
                               cl.sendMessage(msg.to, str(helpMessage3))

                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage4 = help4()
                               cl.sendMessage(msg.to, str(helpMessage4))

                        elif cmd == "help5":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage5 = help5()
                               cl.sendMessage(msg.to, str(helpMessage5))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┏━━━━━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰🎯 Arif Suleng Bots 🎯🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["sticker"] == True: md+="┃🎯┃💢┃ On  Sticker\n"
                                else: md+="┃🎯┃💢┃ Off   Sticker\n"
                                if wait["contact"] == True: md+="┃🎯┃💢┃ On  Contact\n"
                                else: md+="┃🎯┃💢┃ Off   Contact\n"
                                if wait["detectMention"] == True: md+="┃🎯┃💢┃ On  Respon\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                else: md+="┃🎯┃💢┃ Off   Respon\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["autoJoin"] == True: md+="┃🎯┃💢┃ On  Autojoin\n"
                                else: md+="┃🎯┃💢┃ Off   Autojoin\n"
                                if settings["autoJoinTicket"] == True: md+="┃🎯┃💢┃ On  Jointicket\n"
                                else: md+="┃🎯┃💢┃ Off   Jointicket\n"
                                if settings["unsendMessage"] == True: md+="┃🎯┃💢┃ On  Unsend\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                else: md+="┃🎯┃💢┃ Off   Unsend\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["autoAdd"] == True: md+="┃🎯┃💢┃ On  Autoadd\n"
                                else: md+="┃🎯┃💢┃ Off   Autoadd\n"
                                if msg.to in welcome: md+="┃🎯┃💢┃ On  Welcome\n"
                                else: md+="┃🎯┃💢┃ Off   Welcome\n"
                                if wait["autoLeave"] == True: md+="┃🎯┃💢┃ On  Autoleave\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                else: md+="┃🎯┃💢┃ Off   Autoleave\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                if msg.to in protect["pqr"]: md+="┃🎯┃💢┃ On  Url\n"
                                else: md+="┃🎯┃💢┃ Off   Url\n"
                                if msg.to in protect["proall"]: md+="┃🎯┃💢┃ On  Proall\n"
                                else: md+="┃🎯┃💢┃ Off  Proall\n"
                                if msg.to in protect["protect"]: md+="┃🎯┃💢┃ On  Protect\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                else: md+="┃🎯┃💢┃ Off   Protect\n┃━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                if msg.to in protect["pinv"]: md+="┃🎯┃💢┃ On  invite\n"
                                else: md+="┃🎯┃💢┃ Off   Invite\n"
                                if msg.to in protect["antijs"]: md+="┃🎯┃💢┃ On  Js\n"
                                else: md+="┃🎯┃💢┃ Off  Js\n"
                                if msg.to in protect["protectname"]: md+="┃🎯┃💢┃ On  Protectname\n"
                                else: md+="┃🎯┃💢┃ Off  Protectname\n"
                                if msg.to in protect["ghost"]: md+="┃🎯┃💢┃ On  Ghost\n"
                                else: md+="┃🎯┃💢┃ Off  Ghost\n"
                                if msg.to in protectcancel: md+="┃🎯┃💢┃ On  Protectcancel\n┏━━━━━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Creator : Arif Suleng🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                else: md+="┃🎯┃💢┃ Off  Protectcancel\n┏━━━━━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Creator : Arif Suleng🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━━━━━\n"
                                cl.sendMessage(msg.to, md+"\n🔰Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔰Time  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")

                        elif cmd == "creator" or text.lower() == 'creator':
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Creator : Arif Suleng🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendMention(msg.to, sender, "My Creator :\n\nArif Suleng Bots\nhttps://line.me/ti/p/~raccell19")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "aku" or text.lower() == 'gue':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               contact = cl.getContact(sender)
                               cl.sendMessage(to, '{}'.format(contact.displayName),contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+cl.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~raccell19', 'type': 'mt', 'subText': "{}".format(contact.statusMessage), 'a-installUrl': 'https://line.me/ti/p/~raccell19', 'a-installUrl': 'https://line.me/ti/p/~raccell19', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~raccell19', 'i-linkUri': 'https://line.me/ti/p/~raccell19', 'id': 'mt000000000a6b79f9', 'text': '{}'.format(contact.displayName), 'linkUri': 'https://line.me/ti/p/~raccell19'}, contentType=19)
                               path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                               image = 'http://dl.profile.line.naver.jp'+path
                               cl.sendImageWithURL(msg.to, image)

                        elif cmd == "me" or text.lower() == 'saya':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:                                               
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                                image = 'http://dl.profile.line.naver.jp'+path
                                cl.sendImageWithURL(msg.to, image)
                                                                       
                        elif text.lower() == "mymid":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'ass':
                               #cl.sendMessage(msg.to, "Assallamu'alaikum Wr. Wb")
                               cl.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'wss':
                               #cl.sendMessage(msg.to, "Wa'alaikumsallam.Wr,Wb")
                               cl.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'iya':
                               cl.sendMessage(msg.to, "Jangan Iya Iya Mulu Beneran Ngerti Nggak")
                        elif text.lower() == 'sue':
                               cl.sendMessage(msg.to, "Sue Tuh Makana Apa Ya Kok sering Diomongin Orang Sana Sini")
                        elif text.lower() == 'sinyal':
                               cl.sendMessage(msg.to, "Hahaha Lelet Kan....??? Makanya Beli Tower Kak...???")
                        elif text.lower() == 'asem':
                               cl.sendMessage(msg.to, "Kok Asem Kak...??? Mandi Dulu Sono...Bau Nihhh")
                        elif text.lower() == 'koplak':
                               cl.sendMessage(msg.to, "Gimana Gak Koplak Obatnya Sudah Habis Yang Dari RS Gila Kemarin")
                        elif text.lower() == 'dudul':
                               cl.sendMessage(msg.to, "Iya Wajar Lah Kak... Gmn Gak Dudul Dia Kurang Anu")
                        elif text.lower() == 'pm':
                               cl.sendMessage(msg.to, "Naahh Loocchh Mulai Nih Main PM Bikin Anu Bae Kak....??? Hihihi")
                        elif text.lower() == 'sudah':
                               cl.sendMessage(msg.to, "Lha Kok Sudah... Lha Aku Kok Belum Gmn Nih... Trus Aku Kudu Piye")
                        elif text.lower() == 'belum':
                               cl.sendMessage(msg.to, "Lho Masak Sih Belum...!! Prasaan Tadi Sudah Loo Hayo Jujur...")
                        elif text.lower() == 'nikung on':
                               cl.sendMessage(msg.to, "Already Nikung Rondo , Perawan ,Banci ,Bencong Dll")
                        elif text.lower() == 'kojom on':
                               cl.sendMessage(msg.to, "All Ready Kojom Kapan Saja Oke Hahaha")
                        elif text.lower() == 'mojok on':
                               cl.sendMessage(msg.to, "All Ready Mojokin Bojone Uwong hhhhh")
                        elif text.lower() == 'rondo on':
                               cl.sendMessage(msg.to, "All Ready Nikung Rondo Digroup Ini")
                        elif text.lower() == 'slingkuh on':
                               cl.sendMessage(msg.to, "All Ready Slingkuh ... Lho kok Slingkuh Kembali Off")
                        elif text.lower() == 'nikung off':
                               cl.sendMessage(msg.to, "Nikung Berhasil Dinon Actifkan Digroup Ini")
                        elif text.lower() == 'rondo off':
                               cl.sendMessage(msg.to, "Kojom Sama Rondo Dinon Actifkn")
                        elif text.lower() == 'mojok off':
                               cl.sendMessage(msg.to, "Berhasil Menonactifkan Kebiasaan Mojok")
                        elif text.lower() == 'iya':
                               cl.sendMessage(msg.to, "Jangan Iya Iya Mulu Beneran Ngerti Nggak")
                        elif text.lower() == 'bot':
                               cl.sendMessage(msg.to, "All Bots Siap anu Nganu Kak Wkwkwk")
                        elif text.lower() == 'pagi':
                               cl.sendMessage(msg.to, "Pagi Juga & Selamat Actifitas Guys")
                        elif text.lower() == 'siang':
                               cl.sendMessage(msg.to, "Selamat Siang Juga Jangan Lupa Makan")
                        elif text.lower() == 'sore':
                               cl.sendMessage(msg.to, "Selamat Sore Juga Jangan Lupa Gi Mandi")
                        elif text.lower() == 'malam':
                               cl.sendMessage(msg.to, "Selamat Malam Juga Met Bobok Met Istrahat")
                        elif text.lower() == 'order':
                               cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Team Arif Suleng Bots 🎯 \n┗━━━━━━━━━━━━━━━━━━━━\n┃🎯 Open Order Segala Bot\n┃🎯SB Only Biasa\n┃🎯SB Only Pro\n┃🎯SB Unly Template\n┃━━━━━━━━━━━━━━━━━━━━\n┃🎯Jenis Bot Protect Group\n┃🎯1Sb 3bot 2Ghost 1Ajs\n┃🎯1Sb 5Bot 2Ghost 1Ajs\n┃🎯1Sb 6Bot 2Ghost 2Ajs\n┃🎯1Sb 5Bot 5Ghost 2Ajs\n┃🎯1Sb 13Bot 3Ghost 2Ajs\n┃🎯1Sb 5bot 1Ajs\n┃🎯1Sb 7bot 1Ajs\n┃🎯1Sb 8bot 2Ajs\n┃🎯1Sb 10Bot 2Ajs\n┃🎯1Sb 12Bot 2Ajs\n┃━━━━━━━━━━━━━━━━━━━━\n┃🎯SC Bisa Request Hubungi\n┃🎯https://line.me/ti/p/~raccell19\n┗━━━━━━━━━━━━━━━━━━━━")


                        elif ("mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Kepo " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, mid)
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Emid)
                              cl.sendContact(to, Zmid)
                               
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              k1.sendMessage(msg.to,Amid)
                              k2.sendMessage(msg.to,Bmid)
                              k3.sendMessage(msg.to,Cmid)
                              k4.sendMessage(msg.to,Dmid)
                              k5.sendMessage(msg.to,Emid)
                              cl.sendMessage(msg.to,Zmid)
                               
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                      ki.rejectGroupInvitation(gid)
                                      ka.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  k1.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  k2.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  k3.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  k4.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  k5.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  sw.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  k1.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  k2.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  k2.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  k3.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  k4.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  k5.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  sw.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")

                        elif text.lower() == "remove":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   k1.removeAllMessages(op.param2)
                                   k2.removeAllMessages(op.param2)
                                   k3.removeAllMessages(op.param2)
                                   k4.removeAllMessages(op.param2)
                                   k5.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot 1 Sukses Clear Chat 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                                   k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot 2 Sukses Clear Chat 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                                   k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot 3 Sukses Clear Chat 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                                   k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot 4 Sukses Clear Chat 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                                   k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot 5 Sukses Clear Chat 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                               except:
                                   pass

                        elif text.lower() == "clearchat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   k1.removeAllMessages(op.param2)
                                   k2.removeAllMessages(op.param2)
                                   k3.removeAllMessages(op.param2)
                                   k4.removeAllMessages(op.param2)
                                   k5.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Done Clear Chat 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                               except:
                                   pass

                        elif cmd.startswith("bcast "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"Broadcast \n\n" + str(pesan))

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, " Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "Sname change \n\nSname succes change to {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "Succes Reset Sname ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Proses Runing Ulang Guys 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Done...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in owner or msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "Team Suleng Grup Info\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"FRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯 Kode QR Ditutup Guys 🎯 \n┗━━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃Nama : "+str(x.name)+ "\n┗━━━━━━━━━━━━━━━━━━━━\n Url grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#

                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃Silahkan Kirim Pp Group \n┗━━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "upgue":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃Silahkan Kirim Pp Group \n┗━━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "ccp":
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = False
                                cl.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "cvp":
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                Setmain["ARvideo"][mid] = False
                                cl.sendMessage(msg.to,"Kirim videonya.....")

                        elif cmd.startswith("myname "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃Sukses Update Your Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")

                        elif cmd.startswith("getmimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendMessage(msg.to,ret_)

                        elif cmd == "restart2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.sendMention(msg.to, sender, "「 Restarting 」\nUser ", "\nTunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["ARGfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ARGfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send picture")
                      
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                settings["ARfoto"][Amid] = True
                                k1.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                settings["ARfoto"][Bmid] = True
                                k2.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                settings["ARfoto"][Cmid] = True
                                k3.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                settings["ARfoto"][Dmid] = True
                                k4.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot5up":
                            if msg._from in admin:
                                settings["ARfoto"][Emid] = True
                                k5.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot6up":
                            if msg._from in admin:
                                settings["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send picture")

                        elif cmd.startswith("bname "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile = k2.getProfile()
                                profile = k3.getProfile()
                                profile = k4.getProfile()
                                profile = k5.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k2.updateProfile(profile)
                                k3.updateProfile(profile)
                                k4.updateProfile(profile)
                                k5.updateProfile(profile)
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃All Bots Sukses Update \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")

                        elif cmd.startswith("b1name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃B1 Sukses Update Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")

                        elif cmd.startswith("b2name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃B2 Sukses Update Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")

                        elif cmd.startswith("jname "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile = sw1.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw1.updateProfile(profile)
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃AJS Sukses Update Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")

                        elif cmd.startswith("b3name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃B3 Sukses Update Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")
                                
                        elif cmd.startswith("b4name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k4.getProfile()
                                profile.displayName = string
                                k4.updateProfile(profile)
                                k4.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃B4 Sukses Update Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")
   
                        elif cmd.startswith("b5name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k5.getProfile()
                                profile.displayName = string
                                k5.updateProfile(profile)
                                k5.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━━\n┃B5 Sukses Update Name \n┗━━━━━━━━━━━━━━━━━━━━\n" + string + "")

#===========BOT UPDATE============#
                        elif cmd == "sepinya" or text.lower() == 'sepi':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7,nm8,nm9,nm10,nm11,nm12,nm13,nm14,nm15, jml = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (150, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, len(nama)-1):
                                       nm8 += [nama[q]]                                       
                                   mentionMembers(msg.to, nm9)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, len(nama)-1):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 100):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, len(nama)-1):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                               if jml > 200 and jml < 220:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, len(nama)-1):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                               if jml > 220 and jml < 240:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, len(nama)-1):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                               if jml > 240 and jml < 260:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, len(nama)-1):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                               if jml > 260 and jml < 280:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, 280):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                                   for w in range (280, len(nama)-1):
                                       nm15 += [nama[w]]
                                   mentionMembers(msg.to, nm15)
                               if jml > 280 and jml < 300:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 220):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 240):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 260):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, 280):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                                   for w in range (280, 300):
                                       nm15 += [nama[w]]
                                   mentionMembers(msg.to, nm15)
                                   for x in range (300, len(nama)-1):
                                       nm16 += [nama[x]]
                                   mentionMembers(msg.to, nm16)

                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\n┏━━━━━━━━━━━━━━━━━━━\n┃ Anti JS All Ready Stay\n┃ Di Group "+str(ginfo.name)+"\n┃ Anti JS Siap Backup\n┗━━━━━━━━━━━━━━━━━━━")
                                except:
                                    pass

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━\n┃ 🎯🔰🎯 Suleng Bots 🎯🔰🎯\n┗━━━━━━━━━━━━━━━━━━━\n\n ━━━━━━━━━━━━━━━━━━━━ \n┃ 🎯Jumlah Owner🎯\n ━━━━━━━━━━━━━━━━━━━━ \n\n"+ma+"\n ━━━━━━━━━━━━━━━━━━━━ \n┃ 🎯Jumlah Admin🎯\n ━━━━━━━━━━━━━━━━━━━━\n\n"+mb+"\n ━━━━━━━━━━━━━━━━━━━━ \n┃ 🎯Jumlah Staff🎯\n ━━━━━━━━━━━━━━━━━━━━\n\n"+mc+"\n┏━━━━━━━━━━━━━━━━━━━\n┃ { %s } Adminlist Suleng Bots\n┗━━━━━━━━━━━━━━━━━━━" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                mg = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                g = 0
                                f = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["antijs"]
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"Settings Protection\n\nProurl :\n"+ma+"\nProall:\n"+mb+"\nProtect:\n"+mf+"\nProtect Cancel:\n"+mc+"\nProinvite:\n"+md+"\nProtectJS:\n"+mg+"\nProtectlist %s Grup protect" %(str(len(protect["pqr"])+len(protect["protect"])+len(protect["antijs"])+len(protect["proall"])+len(protectcancel)+len(protect["pinv"]))))

                        elif cmd == "name":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                k1.sendMessage(msg.to,responsename1)
                                k2.sendMessage(msg.to,responsename2)
                                k3.sendMessage(msg.to,responsename3)
                                k4.sendMessage(msg.to,responsename4)
                                k5.sendMessage(msg.to,responsename5)

                        elif cmd == "in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k5.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k5.updateGroup(G)
                                cl.sendMessage(msg.to, "Allpro on")
                                k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 1 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 2 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 3 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 4 ) Hadir Gan..??? ?? \n┗━━━━━━━━━━━━━━━━━━━")
                                k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 5 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "invite":
                            anggota = [Amid,Bmid,Cmid,Dmid,Emid]
                            cl.inviteIntoGroup(msg.to, anggota)
                            k1.acceptGroupInvitation(msg.to)
                            k2.acceptGroupInvitation(msg.to)
                            k3.acceptGroupInvitation(msg.to)
                            k4.acceptGroupInvitation(msg.to)
                            k5.acceptGroupInvitation(msg.to)
                            k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 1 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                            k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 2 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                            k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 3 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                            k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 4 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                            k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 5 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 1 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                               k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 2 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                               k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 3 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                               k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 4 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                               k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Bot ( 5 ) Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "jrespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sw.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Anti JS Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "ajs bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif cmd == "ajs in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)
                                sw.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Anti JS Hadir Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")

                        elif msg.text in ["Cancel all"]:
                             if msg.toType == 2:
                                 group = cl.getGroup(msg.to)
                                 gMembMids = [contact.mid for contact in group.invitee]
                                 for _mid in gMembMids:
                                     cl.cancelGroupInvitation(to,[_mid])
                                     time.sleep(0.0002)
                                 cl.sendMessage(to,"┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Cancel All Invite Gan..??? 🎯 \n┗━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "cancel":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.cancelGroupInvitation(msg.to, [Xmid,Zmid])
                                    contact = cl.getProfile()
                                    mids = [contact.mid]
                                    cl.sendMessage(to,"┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Anti JS Sukses Di Cancel 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                    name = "Protect Anti JS"
                                    url = 'https://line.me/ti/p/~raccell19'
                                    iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus))
                                    text = "Berhasil Mengeluarkan AntiJS Dari Group"
                                    sendMentionV10(msg.to, str(text), str(name), str(url), str(iconlink))
                                except:	
                                    pass

                        elif cmd == "my bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Kami Team Arif Suleng Bots Pamit Dulu All\nSemoga Dilain Waktu Kita Bisa Ketemu Kembali..... Selamat Tinggal  "+str(G.name))
                                cl.leaveGroup(msg.to)
                                k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k1.leaveGroup(msg.to)
                                k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k2.leaveGroup(msg.to)
                                k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k3.leaveGroup(msg.to)
                                k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k4.leaveGroup(msg.to)
                                k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k5.leaveGroup(msg.to)

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k1.leaveGroup(msg.to)
                                k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k2.leaveGroup(msg.to)
                                k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃?? Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k3.leaveGroup(msg.to)
                                k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k4.leaveGroup(msg.to)
                                k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Pamit Pulang Dulu 🎯 \n┗━━━━━━━━━━━━━━━━━━\n\n Group  "+str(G.name))
                                k5.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, " Silahkan invite Ownernya ")
                                        cl.leaveGroup(i)
                                        cl.sendMessage(to,"Succes leave group " +h)

                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "Time Respon \n\nGet Profile\n   %.10f\nGet Contact\n   %.10f\nGet Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━━\n┃🎯 Menghitung Tikungan Guys 🎯 \n┗━━━━━━━━━━━━━━━━━━━━━")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━\n┃ Total Slingkuhan\n┃ {}\n┗━━━━━━━━━━━━━━━".format(str(elapsed_time/10)))
                               k1.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━\n┃ Slingkuhan 1 Ready\n┃ {}\n┗━━━━━━━━━━━━━━━".format(str(elapsed_time/10)))
                               k2.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━\n┃ Slingkuhan 2 Ready\n┃ {}\n┗━━━━━━━━━━━━━━━".format(str(elapsed_time/10)))
                               k3.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━\n┃ Slingkuhan 3 Ready\n┃ {}\n┗━━━━━━━━━━━━━━━".format(str(elapsed_time/10)))
                               k4.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━\n┃ Slingkuhan 4 Ready\n┃ {}\n┗━━━━━━━━━━━━━━━".format(str(elapsed_time/10)))
                               k5.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━\n┃ Slingkuhan 5 Ready\n┃ {}\n┗━━━━━━━━━━━━━━━".format(str(elapsed_time/10)))
                               cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━━\n┃🎯 Sungguh Terlalu Kau Rhoma 🎯 \n┗━━━━━━━━━━━━━━━━━━━━━")

                        elif cmd == "lurk on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SKreadPoint'][msg.to] = msg_id
                                 Setmain['SKreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SKreadPoint'][msg.to]
                                 del Setmain['SKreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['SKreadPoint']:
                                if Setmain['SKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['SKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "{ Team Arif Suleng Bots }\n\n┏━━━━━━━━━━━━━━━━━\n┃🎯CCTV Diaktifkan Guys🎯\n┗━━━━━━━━━━━━━━━━━\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "{ Team Arif Suleng Bots }\n\n┏━━━━━━━━━━━━━━━━━\n┃🎯 CCTV Di Non Actifkan 🎯\n┗━━━━━━━━━━━━━━━━━\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "{ Team Arif Suleng Bots }\n\n┏━━━━━━━━━━━━━━━━━\n┃🎯 CCTV Belum Di Set 🎯\n┗━━━━━━━━━━━━━━━━━")

#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim video nya...")
                                else:
                                    cl.sendMessage(to, "video itu sudah dalam list")
                        elif cmd.startswith("dellvideo "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   cl.sendMessage(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   cl.sendMessage(to, "video itu tidak ada dalam list")

                        elif cmd == "listvideo":
                                no = 0
                                ret_ = "Daftar video\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} video".format(str(len(images)))
                                cl.sendMessage(to, ret_)
#=========== [ Add Audio] ============#
                        elif cmd.startswith("addmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim mp3 nya...") 
                                else:
                                    cl.sendMessage(to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                                else:
                                    cl.sendMessage(to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                                no = 0
                                ret_ = "Daftar Lagu\n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\nTotal {} Lagu".format(str(len(audios)))
                                cl.sendMessage(to, ret_)
 #=========== [ Add sticker] ============#                   
                        elif cmd.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim stickernya...") 
                                else:
                                    cl.sendMessage(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    cl.sendMessage(to, "Sticker itu tidak ada dalam list") 
                                                   
                        elif cmd == "liststicker":
                                no = 0
                                ret_ = " Daftar Sticker \n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + sticker.title() + "\n"
                                ret_ += "\nTotal {} Stickers".format(str(len(stickers)))
                                cl.sendMessage(to, ret_)
#=========== [ Hiburan] ============#  
                        elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(sender), str(result), 'Auto Like by dhenza')
                                    cl.sendMessage(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))
                                                                                 
                        elif text.lower().startswith("music "):
                            try:
                                search = text.lower().replace("musik","")
                                r = requests.get("https://rest.farzain.com/api/joox.php?apikey=rambu&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                cl.sendMessage(msg.to, "Searching mp3 done..")
                            except Exception as error:
                            	cl.sendMessage(msg.to, "「 Result Error 」\n" + str(error))
                        
                        elif cmd.startswith("profilesmule "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)
                            
                        elif cmd.startswith("profileig "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                cl.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                cl.sendMessage(msg.to, str(njer))
                                                                                    
                        elif cmd.startswith("mp4 "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                                
                        elif cmd.startswith("img food "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))
                        
                        elif cmd.startswith("cekdate "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"Informasi™\n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("jumlah "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Spamtag change to " +strnum)

                        elif cmd.startswith("spamcall "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 5000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 5000")
                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 10:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "{ Team Arif Suleng Bots }\n\nBerhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        #elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 5000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")
                                    
#                        elif cmd.startswith("spaminvite"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = cl.findContactsByUserid(userid)
                                    cl.findAndAddContactsByUserid(userid)
                                    if jumlah <= 5000:
                                        for var in range(0,jumlah):
                                            try:
                                                cl.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = cl.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    cl.leaveGroup(grup.id)
                                                	    cl.sendText(to,"@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))

                        elif 'Gift ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 5000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Sambutan Diactifkan 🎯 \n┗━━━━━━━━━━━━━━━━━━━"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Arif Suleng Bots🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\n\n┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Sambutan Diactifkan 🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "{ Team Arif Suleng Bots }\n\nWelcome Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Arif Suleng Bots🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\n\n┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Sambutan Dinon actifkan 🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Arif Suleng Bots🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\n\n┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Sambutan Belum Di Set🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━"
                                    cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Arif Suleng Bots🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\n\n┏━━━━━━━━━━━━━━━━━━━━\n┃🎯🔰Sambutan Dinon Actifkan🔰🎯 \n┗━━━━━━━━━━━━━━━━━━━━\n" + msgs)

                        elif 'Skurl ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Skurl ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "{ Team Arif Suleng Bots }\n\nSKurl has been active"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "{ Team Arif Suleng Bots }\n\nSkurl telah active\n\ndi group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "{ Team Arif Suleng Bots }\n\nSkurl deactive\n\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "{ Team Arif Suleng Bots }\n\nSkurl has been deactive"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "Protect has been active"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect Active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "Proall has been active"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect all active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect all deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect all has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "{ Team Arif Suleng Bots }\n\nProtect cancel has been active "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "{ Team Arif Suleng Bots }\n\nProtect cancel active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "{ Team Arif Suleng Bots }\n\nProtect cancel deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "{ Team Arif Suleng Bots }\n\nProtect cancel has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proname ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protectname ','')
                              if spl == 'on':
                                  if msg.to in protectname:
                                       msgs = "{ Team Arif Suleng Bots }\n\nProtect name has been active "
                                  else:
                                       protectname.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "{ Team Arif Suleng Bots }\n\nProtect name active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectname:
                                         protectname.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "{ Team Arif Suleng Bots }\n\nProtect name deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "{ Team Arif Suleng Bots }\n\nProtect name has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Skinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Skinvite ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "skinvite has been active"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "skurl active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "skinvite deactive\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "skinvite has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in protect["ghost"]:
                                       msgs = "Protect Ghost Di Actifkan"
                                  else:
                                       protect["ghost"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Ghost Telah Actif 🔰\n┗━━━━━━━━━━━━━━━━\n\n🔰 Di Group 🔰 " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━\n┃🔰Elloalea Bots🔰\n┗━━━━━━━━━━━━━━━━\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["ghost"]:
                                         protect["ghost"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Ghost Di Non Actifkan 🔰\n┗━━━━━━━━━━━━━━━━\n\n🔰 Dari Group ?? " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Di Non Actifkan "
                                    cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━\n┃🔰Elloalea Bots🔰\n┗━━━━━━━━━━━━━━━━\n\n" + msgs)

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protect["antijs"]:
                                       msgs = "{ Team Arif Suleng Bots }\n\nProtect Anti JS Di Actifkan"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Anti JS Actif 🔰\n┗━━━━━━━━━━━━━━━━\n\n🔰 Di Group 🔰 " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━\n┃🔰Arif Suleng Bots🔰\n┗━━━━━━━━━━━━━━━━\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Anti JS Non Actif 🔰\n┗━━━━━━━━━━━━━━━━\n\n🔰 Di Group 🔰 " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS off "
                                    cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━\n┃🔰Arif Suleng Bots🔰\n┗━━━━━━━━━━━━━━━━\n\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                      msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protectcancel"]:
                                       msgs = ""
                                  else:
                                       protect["protectcancel"].append(msg.to)
                                  if msg.to in protect["protectname"]:
                                       msgs = ""
                                  else:
                                       protect["protectname"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["ghost"]:
                                      msgs = ""
                                  else:
                                      protect["ghost"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect on \n\ndi group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Protect Link On\n┃🔰 Protect Cancel On\n┃🔰 Protect Kick On\n┃🔰 Protect Invite On\n┃🔰 Protect Name On\n┗━━━━━━━━━━━━━━━━\n🔰 Di Group 🔰\n\n" +str(ginfo.name)
                                  cl.sendMessage(msg.to, "┏━━━━━━━━━━━━━━━━\n┃🔰Allpro Arif Suleng🔰\n┗━━━━━━━━━━━━━━━━\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protectname"]:
                                         protect["protectname"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protectcancel"]:
                                         protect["protectcancel"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["ghost"]:
                                         protect["ghost"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Protect Link Off\n┃🔰 Protect Cancel Off\n┃🔰 Protect Kick Off\n┃🔰 Protect Invite Off\n┃🔰 Protect Name Off\n┗━━━━━━━━━━━━━━━━\n🔰 Di Group 🔰\n\n" +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "┏━━━━━━━━━━━━━━━━\n┃🔰 Protect Link Off\n┃🔰 Protect Cancel Off\n┃🔰 Protect Kick Off\n┃🔰 Protect Invite Off\n┃🔰 Protect Name Off\n┗━━━━━━━━━━━━━━━━\n🔰 Di Group 🔰\n\n" +str(ginfo.name)
                                    cl.sendMessage(msg.to, "Nonactive\n" + msgs)

#===========KICKOUT============#       
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Bubar" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Bubar","")                                 
                                 gs = k1.getGroup(msg.to)
                                 gs = k2.getGroup(msg.to)
                                 gs = k3.getGroup(msg.to)
                                 gs = k4.getGroup(msg.to)
                                 gs = k5.getGroup(msg.to)
                                 gs = k1.getGroup(msg.to)
                                 gs = k2.getGroup(msg.to)
                                 gs = k3.getGroup(msg.to)
                                 gs = k4.getGroup(msg.to)
                                 gs = k5.getGroup(msg.to)
                                 gs = k1.getGroup(msg.to)
                                 gs = k2.getGroup(msg.to)
                                 gs = k3.getGroup(msg.to)
                                 gs = k4.getGroup(msg.to)
                                 gs = k5.getGroup(msg.to)
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendMessage(msg.to,"Limit boss")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   suleng= [k1,k2,k3,k4,k5]
                                                   kicker=random.choice(suleng)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   cl.sendMessage(msg.to, str(error))

                        elif text.lower() == 'suleng':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendMessage(msg.to, "Proses Cleaner All Bots")
                                  cl.sendMessage(msg.to, " Arif Suleng Bots \nmember : " +str(len(ginfo.members)) + " \nFuck you...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace('Bubar','')
                                  gs = k1.getGroup(msg.to)
                                  gs = k2.getGroup(msg.to)
                                  gs = k3.getGroup(msg.to)
                                  gs = k4.getGroup(msg.to)
                                  gs = k5.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	cl.sendMessage(msg.to, "Nothing member")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass
                                                      
                        elif text.lower() == 'killban':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "Limit bos")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                                
                        elif "Mainkan " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      ki.kickoutFromGroup(msg.to,[target])
                                      ki.findAndAddContactsByMid(target)
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
                                       
                        elif cmd == "gas":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               #cl.sendMessage(msg.to, "Asallamu'alsikum wr wb\nHallo!!! Sory Room Kalian\n\nKebanyakan Anu Siihh\nTeam Suleng\nMau Bersih Bersih GC\nNo Koment \nNo Baper\nRausah Kokean Cangkem \nNo Desah \nNo Sponsor\nNo Heaters\nRoom Bokep iki\nRoom Bejat\nRoom Gak Jelas\nSiap Kami Bantai\n\n\n\n Fuck You...\nKenapa Pada diam\nTangkis Jgn Hanya Lihat Doang\n\n\nDasar Room Peak Gak Jelas\nSory Boss!!!\nGC Kalian Mau Saya Sita...!!!\n\n\n Sallam Dari Kami Suleng Team Bots\n\nHadir Diroom Anda\n\nRata Gak Rata Penting Anu \nRata Kami Senang\nGak Rata Tunggu Kedatangan Kami Lagi\n\n\nSallsm Dancok Asu To Kalian \n\n\n>>>>>>GO!!! <<<<<<\n\n\nCREATOR\n\n<<<<<<<<<<Suleng Bots>>>>>>>>>>\n\nhttp://line.me/ti/p/~raccell19\nhttp://line.me/ti/p/~suleng28")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
#===========ADMIN ADD============
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                             
                                           cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━━\n┃🎯 Berhasil Menambahkan Admin 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Berhasil Menambahkan Staff 🎯 \n┗━━━━━━━━━━━━━━━━━━")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in ArifSuleng:
                                       try:
                                           #admin.remove(target)
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in ArifSuleng:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\nBerhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in ArifSuleng:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staff on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Bot on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Succes Addbot")
                                       except:
                                           pass

                        elif ("Adminexpl on " in msg.text):
                            if msg._from in owner or msg_from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel admin")
                                       except:
                                           pass

                        elif ("Staffexpl on " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel staff")
                                       except:
                                           pass

                        elif ("Botexpl on " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel Bots")
                                       except:
                                           pass
  #====================================#                                         
                        elif cmd == "autojoin on":
                            if msg._from in owner:
                                settings["autoJoin"] = True
                                cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━\n┃🎯 Auto Join On 🎯 \n┗━━━━━━━━━━━━━━━━━")
                        elif cmd == "autojoin off":
                            if msg._from in owner:	
                                settings["autoJoin"] = False
                                cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━\n┃🎯 Auto Join Off 🎯 \n┗━━━━━━━━━━━━━━━━━")
                        elif cmd == "autoblock on":
                           if msg._from in owner:
                                settings["autoBlock"] = True
                                cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━\n┃🎯 Auto Block On 🎯 \n┗━━━━━━━━━━━━━━━━━")
                        elif cmd == "autoblock off":    
                            if msg._from in owner: 	
                                settings["autoBlock"] = False
                                cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━\n┃🎯 Auto Block Off 🎯 \n┗━━━━━━━━━━━━━━━━━")
                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Chek Post Diactifkan 🎯 \n┗━━━━━━━━━━━━━━━━━━")
                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Chek Post Dimatikan 🎯 \n┗━━━━━━━━━━━━━━━━━━")
                        elif cmd == "unsend on":
                       	 if msg._from in owner:
                                 settings["unsendMessage"] = True
                                 cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Unsend Di Actifkan 🎯 \n┗━━━━━━━━━━━━━━━━━━")
                        elif cmd == "unsend off":
                            if msg._from in owner:
                                 settings["unsendMessage"] = False
                                 cl.sendMessage(to, "┏━━━━━━━━━━━━━━━━━━\n┃🎯 Unsen Di Matikan 🎯 \n┗━━━━━━━━━━━━━━━━━━")
#==================================#
                        elif cmd == "admin on" or text.lower() == 'admin on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\nSilahkan Kirim Contactnya")

                        elif cmd == "adminexpl on" or text.lower() == 'adminexpl on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff on" or text.lower() == 'staff on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\nSilahkan Kirim Contactnya")

                        elif cmd == "staffexpl on" or text.lower() == 'staffexpl on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\nSilahkan Kirim Contactnya")

                        elif cmd == "bot on" or text.lower() == 'bot on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\nMonggo Send contact")

                        elif cmd == "botexpl on" or text.lower() == 'botexpl on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"{ Team Arif Suleng Bots }\n\nMonggo Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Arif Suleng Bots 🎯 \n┗━━━━━━━━━━━━━━━━━━\n┏━━━━━━━━━━━━━━━━━━\n┃🎯 Proses Cliner Bot 🎯 \n┗━━━━━━━━━━━━━━━━━━")
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Arif Suleng Bots 🎯 \n┗━━━━━━━━━━━━━━━━━━\n┏━━━━━━━━━━━━━━━━━━\n┃🎯 Refresh Done Gan 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                     
                        elif cmd == "spaminvite on" or text.lower == 'spaminvite on':
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                cl.sendMessage(msg.to, "Send Contact to spam grup..")
                                
                        elif cmd == "spaminvite off" or text.lower() == 'spaminvite off':
                            if msg._from in admin:
                                settings["Spaminvite"] = False
                                cl.sendMessage(msg.to, "Send Contact to send grup Off..")
                                
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 No Tag Diactifkan 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 No Tag Dimatikan 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Detect Contact On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Detect Contact Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Respon On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Respon Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Join On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Join Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Leave On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Leave Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Add On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Auto Add Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Detect Sticker On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Detect Sticker Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Join Ticket On 🎯 \n┗━━━━━━━━━━━━━━━━━━")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Join Ticket Off 🎯 \n┗━━━━━━━━━━━━━━━━━━")

#===========COMMAND BLACKLIST============#
                        elif cmd == "ban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                                                
                        elif cmd == "unban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                        elif ("Talkban on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban on" or text.lower() == 'talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "untalkban on" or text.lower() == 'untalkban on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban on" or text.lower() == 'ban on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "unban on" or text.lower() == 'unban on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bl" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Tidak Ada Blacklist 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                    k1.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Tidak Ada Blacklist 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                    k2.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Tidak Ada Blacklist 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                    k3.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Tidak Ada Blacklist 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                    k4.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Tidak Ada Blacklist 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                                    k5.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Tidak Ada Blacklist 🎯 \n┗━━━━━━━━━━━━━━━━━━━")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "%i" % len(ragets)
                              cl.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Sukses Clear Sampah 🎯 \n┗━━━━━━━━━━━━━━━━━━"   +mc)
                              k1.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Sukses Clear Sampah 🎯 \n┗━━━━━━━━━━━━━━━━━━"   +mc)
                              k2.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Sukses Clear Sampah 🎯 \n┗━━━━━━━━━━━━━━━━━━"   +mc)
                              k3.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Sukses Clear Sampah 🎯 \n┗━━━━━━━━━━━━━━━━━━"   +mc)
                              k4.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Sukses Clear Sampah 🎯 \n┗━━━━━━━━━━━━━━━━━━"   +mc)
                              k5.sendMessage(msg.to,"┏━━━━━━━━━━━━━━━━━━\n┃🎯 Sukses Clear Sampah 🎯 \n┗━━━━━━━━━━━━━━━━━━"   +mc)
                        elif text.lower() == 'mas':
                               cl.sendMessage(msg.to, "Kalau kangen Hubungi Arif Suleng Bots Ktik Creator")
#===========COMMAND SET============#
                        elif 'Spesan ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Swelcome ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Srespon ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Srespon ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sspam ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sspam ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ssider ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ssider ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cpesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                               
                        elif cmd == "batre":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, [mid]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, [mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               cl.sendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                               try:k1.inviteIntoGroup(to, [Amid]);has = "OK"
                               except:has = "NOT"
                               try:k1.kickoutFromGroup(to, [Amid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               k1.sendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                               try:k2.inviteIntoGroup(to, [Bmid]);has = "OK"
                               except:has = "NOT"
                               try:k2.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               k2.sendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                               try:k3.inviteIntoGroup(to, [Cmid]);has = "OK"
                               except:has = "NOT"
                               try:k3.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               k3.sendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                               try:k4.inviteIntoGroup(to, [Dmid]);has = "OK"
                               except:has = "NOT"
                               try:k4.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               k4.sendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                               try:k5.inviteIntoGroup(to, [Emid]);has = "OK"
                               except:has = "NOT"
                               try:k5.kickoutFromGroup(to, [Emid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               k5.sendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                               try:sw.inviteIntoGroup(to, [Zmid]);has = "OK"
                               except:has = "NOT"
                               try:sw.kickoutFromGroup(to, [Zmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔌🔋 ██  full 💯 %"
                               else:sil = "🔌█▒ Low 0⃣ %"
                               if has1 == "OK":sil1 = "🔌🔋 ██  full 💯 %"
                               else:sil1 = "🔌█▒ Low 0⃣ %"
                               swsendMessage(to, "Status: Dosamu \n\n⏩ Nikung : Rondo {} \n⏩ Mojokin : Rondo {}".format(sil1,sil))
                            
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = k1.findGroupByTicket(ticket_id)
                                     
    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
