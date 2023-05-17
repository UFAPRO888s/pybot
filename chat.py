
import re,time,random
import gpt4free
#from gpt4free import quora
from gpt4free import Provider , forefront
from googletrans import Translator
translator = Translator()




cmd  = ".bnการเล่นหวย"
prxp = ["กำลังเถียงกันอยู่สักครู่นะ","กำลังประมวลผล","กำลังกินนมจะนอนแย้ว"]
startText = ["กราบเรียนผู้มีอุปการคุณ","สวัสดี","ว่าไง","ยินดีบริการ"]
if cmd.startswith(".bn"):
    inresse = translator.translate(cmd, dest='en')
    response = gpt4free.Completion.create(Provider.You, prompt=inresse)
    resse = translator.translate(response, dest='th')
    contact = "USER"
    print(random.choice(startText)+" "+contact+" \nท่านสามารถขอหวย รับแนวทางหวย ได้ที่นี่\n")
    time.sleep(2)
    print("ChatGPT-V5 & กุมารทอง-สายใต้\n"+random.choice(prxp)+"\n....\nรับแนวทางหวยประเภทไหน\nให้พิมพ์ หวย ตามด้วยชื่อหวย")
    time.sleep(2)
    print(resse.text)                    
                