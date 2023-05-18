
import re,time,random,requests
from datetime import datetime, timezone, timedelta
import pytz
import schedule

tz = timezone(timedelta(hours = 7))

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("./AccountCredentials.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://bet-balls-default-rtdb.asia-southeast1.firebasedatabase.app'})
Lottoref = db.reference('playyeeke')
Lottoyeeke05 = db.reference('lotto/KIWI_05')
Lottoyeeke10 = db.reference('lotto/KIWI_10')
Lottoyeeke15 = db.reference('lotto/KIWI_15')

response = requests.get("https://result.huaynaka.net/naga-data/"+now.strftime("%Y/%m/%d")+"/data.json").json()
filtered_arr = [p for p in response['KIWI_05'] if p['results'][0]['digit'] == "-"]
print(filtered_arr[0])

def datxtim(t1x):
    dateexe = t1x.split("T")[0]
    timeexe = t1x.split("T")[1].replace(".000Z", "")
    exetdate = dateexe.split("-")
    exettime = timeexe.split(":")
    t1datetime = datetime(int(exetdate[0]),int(exetdate[1]),int(exetdate[2]),int(exettime[0]),int(exettime[1]),int(exettime[2]),tzinfo=tz)
    return t1datetime

#now.isoformat()



def Pyeekee(msguser,yeekecon_ID,yeekecon_Name,yeekecon_img):
    users_ref = Lottoref.child('users')
    users_ref.set({
        yeekecon_ID: {
            'yeeke_id': yeekecon_ID,
            'yeeke_name': yeekecon_Name,
            'yeeke_img': yeekecon_img,
            'yeeke_point': "",
            'yeeke_play': "",
            'yeeke_play_win': "",
            'yeeke_play_loss': "",
            'yeeke_play_draw': "",
            'yeeke_play_datetime_last': dt_string,
        },
    })
    print("22"+msguser,yeekecon_ID,yeekecon_Name)
    
    
#yeekeeNK10: KIWI_10_068_20230518|5/18/2023, 11:20:00 AM
#yeekeeNK05: 05|141|20230518|5/18/2023, 11:45:00 AM
#BOT_CHECK

def yeekeeLottoNotify(msgyeekee,urlLink):
    response = requests.get(urlLink).json()
    #yeekeRoundNow = datxtim(response['cutoff_datetime'])
    #DateRoundNow = datxtim(now.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
    #roundXS(msgyeekee[1],msgyeekee[2],response)

    
    #print(nowcutoff)
    


# cmd = "155 50x50x50"
# yeeke23 = re.search(r"^\d{2,3}+",cmd)
# if yeeke23:
#     yeekecontact_ID = "111111"
#     yeekecontact_Name = "user111"
#     yeekecontact_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png"
#     Xyeeke2 = Pyeekee(yeeke23.group(),yeekecontact_ID,yeekecontact_Name,yeekecontact_img)
    
numberEmo = [{"num":0,"emo":'0️⃣'},{"num":1,"emo":'1️⃣'},{"num":2,"emo":'2️⃣'},{"num":3,"emo":'3️⃣'},{"num":4,"emo":'4️⃣'},{"num":5,"emo":'5️⃣'},{"num":6,"emo":'6️⃣'},{"num":7,"emo":'7️⃣'},{"num":8,"emo":'8️⃣'},{"num":9,"emo":'9️⃣'}]

# def job():
#     print("I'm working...")
#     #schedule.every(10).seconds.do(job)
#     schedule.every(4).minutes.do(job)
#     schedule.every().hour.do(job)
#     schedule.every().day.at("10:30").do(job)
#     schedule.every(5).to(10).minutes.do(job)
#     schedule.every().monday.do(job)
#     schedule.every().wednesday.at("13:15").do(job)
#     schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#     schedule.every().minute.at(":17").do(job)

#     def job_with_argument(name):
#         print(f"I am {name}")

#     schedule.every(10).seconds.do(job_with_argument, name="Peter")

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

def roundXS(roun,ytype,cutoff,NameLottoType):
    RTextToEmo = roun.replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("8", "9️⃣")
    Rtypetoemo = ytype.replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("8", "9️⃣")
    #Ttexttoemo = [p for p in numberEmo if p['num'] == ytype]
    RoundTextStart = "🟢เปิดรับแทงหวย\nรอบที่ "+RTextToEmo+"\nหวยยี่กี่ "+NameLottoType+"\n🕛 ปิดรับแทง\n"+cutoff+"\n"
    return RoundTextStart