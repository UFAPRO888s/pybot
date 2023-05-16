# -*- coding: utf-8 -*-
import json,traceback,requests,datetime,random,pytz
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("./AccountCredentials.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://bet-balls-default-rtdb.asia-southeast1.firebasedatabase.app'})
poster = ["https://huaynaka.com/wp-content/uploads/2021/10/probenner-huaynaka-new.webp","https://huaynaka.com/wp-content/uploads/2022/03/%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7%E0%B9%81%E0%B8%9A%E0%B8%99%E0%B9%80%E0%B8%99%E0%B8%AD%E0%B8%A3%E0%B9%8C-1.jpg","https://huaynaka.com/wp-content/uploads/2023/01/banner-%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B9%82%E0%B8%AE%E0%B8%88%E0%B8%B4%E0%B8%A1%E0%B8%B4%E0%B8%99%E0%B8%AB%E0%B9%8C.webp","https://huaynaka.com/wp-content/uploads/2023/01/banner-%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7-1024x411.webp","https://huaynaka.com/wp-content/uploads/2023/01/banner-%E0%B8%99%E0%B8%B2%E0%B8%84%E0%B8%B2-1024x411.webp","https://huaynaka.com/wp-content/uploads/2023/01/banner-%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7-1024x411.webp"]
Lottoref = db.reference('lottolatest')
snapshot = Lottoref.get()
#filtered_arr = [p for p in snapshot if p['THREE_UP'] != "-" and p['THREE_UP'] != 'undefined']
#TEMFLEXFLEXSTOCKFORE={"type": "bubble", "size": "kilo", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+filterA['img_fg'], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filterA['title_th'], "size": "lg", "wrap": True},{"type": "text", "text": filterA['announce_datetime_th'], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filterA['THREE_UP'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filterA['TWO_DOWN'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filterA['TWO_UP'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover"}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
  
# def FLEXTIME(type):
#     FLEXALLRE = []
#     filtered_arr = [p for p in snapshot if p['sub_type'] == type and p['THREE_UP'] != "-"]
#     #print(filtered_arr[0])
#     TEMFLEXFLEXSTOCKFORE={"type": "bubble", "size": "kilo", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": filtered_arr[0]["img_fg"], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filtered_arr[0]["title_th"], "size": "lg", "wrap": True},{"type": "text", "text": filtered_arr[0]["announce_datetime_th"], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filtered_arr[0]["THREE_UP"], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filtered_arr[0]["TWO_UP"], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filtered_arr[0]["TWO_DOWN"], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover"}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
#     #print(TEMFLEXFLEXSTOCKFORE)
#     return TEMFLEXFLEXSTOCKFORE

# def FLEXREAV():
#     FLEXALLRE = []
#     filtered_arr = [p for p in snapshot if  p['THREE_UP'] != "-" and p['THREE_UP'] != 'undefined']
#     for filterA in filtered_arr:
#         TEMFLEXFLEXSTOCKFORE={"type": "bubble", "size": "kilo", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": filterA["img_fg"], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filterA["title_th"], "size": "lg", "wrap": True},{"type": "text", "text": filterA["announce_datetime_th"], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filterA["THREE_UP"], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filterA["TWO_UP"], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": filterA["TWO_DOWN"], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover"}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
#         FLEXALLRE.append(TEMFLEXFLEXSTOCKFORE)
#     print(FLEXALLRE)
#     return FLEXALLRE

# FLEXREAV()
def lottoFlex(lottotype):
    response = requests.get('https://bet-balls-default-rtdb.asia-southeast1.firebasedatabase.app/nakalottolatest.json')
    filtered_arr = [p for p in response.json() if p['sub_type'] == lottotype and p['THREE_UP'] != "-" and p['sub_type'] != "LATTE_THAI"]
    FLEXTIMEX={"type": "bubble", "size": "mega", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+filtered_arr[0]['img_fg'], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arr[0]['title_th'], "size": "lg", "wrap": True},{"type": "text", "text": filtered_arr[0]['announce_datetime_th'], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arr[0]['THREE_UP'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arr[0]['TWO_UP'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arr[0]['TWO_DOWN'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover","action": {"type": "uri","label": "huaynaka","uri": "https://tang.huaynaka.com/agent/r39lPewF"}}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
    #print(FLEXTIMEX)
    return FLEXTIMEX
    
def lottoFlexAll():
    FLEXTI = []
    response = requests.get('https://bet-balls-default-rtdb.asia-southeast1.firebasedatabase.app/nakalottolatest.json')
    filtered_arr = [p for p in response.json() if p['THREE_UP'] != "-" and p['THREE_UP'] != "undefined" and p['sub_type'] != "LATTE_THAI"]
    #k = len(filtered_arr)//10
    for filtered_arrX in filtered_arr[0:10]:
        #print(filtered_arrX)
        FLEXTIMEXW={"type": "bubble", "size": "mega", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+filtered_arrX['img_fg'], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arrX['title_th'], "size": "lg", "wrap": True},{"type": "text", "text": filtered_arrX['announce_datetime_th'], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arrX['THREE_UP'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arrX['TWO_UP'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+filtered_arrX['TWO_DOWN'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover","action": {"type": "uri","label": "huaynaka","uri": "https://tang.huaynaka.com/agent/r39lPewF"}}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
        FLEXTI.append(FLEXTIMEXW)
    
    return {"type": "carousel", "contents": FLEXTI}


def glotto():
    
    responseXX = requests.get('https://bet-balls-default-rtdb.asia-southeast1.firebasedatabase.app/nakalottolatest.json')
    #responseX3 = requests.get('https://bet-balls-default-rtdb.asia-southeast1.firebasedatabase.app/lottoX3.json').json()
    #print(responseX,responseX3[0]['number'][0])
    responseX = [p for p in responseXX.json() if p['THREE_UP'] != "-" and p['THREE_UP'] != "undefined" and p['sub_type'] == "LATTE_THAI"]
    FLEXGLOTTO={
            "type": "bubble",
            "size": "giga",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://huaynaka.com/wp-content/uploads/2021/10/probenner-huaynaka-new.webp",
                    "size": "full",
                    "aspectRatio": "100:50",
                    "aspectMode": "cover"
                }
                ],
                "paddingAll": "0px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ผลหวยรัฐบาล ประจำวันที่",
                        "size": "sm",
                        "align": "center",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": ""+responseX[0]['announce_datetime_th'],
                        "align": "center",
                        "size": "lg",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": ""+responseX[0]['THREE_UP'],
                                "align": "center",
                                "size": "4xl",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "รางวัลที่ 1",
                                "size": "sm",
                                "weight": "bold",
                                "align": "center"
                            }
                            ],
                            "backgroundColor": "#FFFFCA",
                            "flex": 2,
                            "cornerRadius": "10px",
                            "spacing": "0px",
                            "borderColor": "#A48000",
                            "borderWidth": "2px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": ""+responseX[0]['THREE_PRE_Z'],
                                "align": "center",
                                "size": "4xl",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "เลขท้าย2ตัว",
                                "size": "sm",
                                "weight": "bold",
                                "align": "center"
                            }
                            ],
                            "flex": 1,
                            "backgroundColor": "#FFFFCA",
                            "cornerRadius": "10px",
                            "spacing": "0px",
                            "borderColor": "#A48000",
                            "borderWidth": "2px"
                        }
                        ],
                        "paddingStart": "30px",
                        "paddingEnd": "30px",
                        "spacing": "md"
                    }
                    ],
                    "margin": "md",
                    "spacing": "sm"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "แทงหวย เว็บหวย นาคา หวยออนไลน์ อัตราจ่ายสูงที่สุด",
                        "align": "center",
                        "size": "xs"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": ""+responseX[0]['TWO_UP'],
                                        "weight": "bold",
                                        "align": "center",
                                        "size": "xxl"
                                    }
                                    ],
                                    "backgroundColor": "#FFFFCA",
                                    "cornerRadius": "5px",
                                    "borderWidth": "2px",
                                    "borderColor": "#A48000"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": ""+responseX[0]['TWO_DOWN'],
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    }
                                    ],
                                    "backgroundColor": "#FFFFCA",
                                    "cornerRadius": "5px",
                                    "borderColor": "#A48000",
                                    "borderWidth": "2px"
                                }
                                ],
                                "spacing": "md"
                            },
                            {
                                "type": "text",
                                "text": "3ตัวหน้า",
                                "size": "sm",
                                "weight": "bold",
                                "align": "center"
                            }
                            ],
                            "spacing": "md"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": ""+responseX[0]['THREE_PRE_X'],
                                        "weight": "bold",
                                        "align": "center",
                                        "size": "xxl"
                                    }
                                    ],
                                    "backgroundColor": "#FFFFCA",
                                    "cornerRadius": "5px",
                                    "borderColor": "#A48000",
                                    "borderWidth": "2px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": ""+responseX[0]['THREE_PRE_Y'],
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    }
                                    ],
                                    "backgroundColor": "#FFFFCA",
                                    "cornerRadius": "5px",
                                    "borderColor": "#A48000",
                                    "borderWidth": "2px"
                                }
                                ],
                                "spacing": "md"
                            },
                            {
                                "type": "text",
                                "text": "3ตัวหน้า",
                                "size": "sm",
                                "weight": "bold",
                                "align": "center"
                            }
                            ],
                            "spacing": "md"
                        }
                        ],
                        "paddingStart": "30px",
                        "paddingEnd": "30px",
                        "spacing": "md"
                    }
                    ],
                    "margin": "lg",
                    "paddingTop": "10px",
                    "paddingBottom": "10px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://huaynaka.com/wp-content/uploads/2021/08/sub-banner-%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%99%E0%B8%B2%E0%B8%84%E0%B8%B2.webp",
                        "size": "full",
                        "aspectRatio": "100:40",
                        "aspectMode": "cover"
                    }
                    ],
                    "paddingTop": "10px"
                }
                ],
                "paddingAll": "0px",
                "background": {
                "type": "linearGradient",
                "angle": "140deg",
                "startColor": "#DDC876",
                "endColor": "#FCF8A3"
                }
                }
            }

    return FLEXGLOTTO


#for dataLotto in snapshot:
    #if dataLotto['THREE_UP'] != "-":
      
      #print(dataLotto)



# LATTE_FOREIGN_HANOI = snapshot['LATTE_FOREIGN_HANOI']
# LATTE_FOREIGN_HANOIEXTRA = snapshot['LATTE_FOREIGN_HANOIEXTRA']
# LATTE_FOREIGN_HANOIVIP = snapshot['LATTE_FOREIGN_HANOIVIP']
# LATTE_FOREIGN_HOCHIMINH = snapshot['LATTE_FOREIGN_HOCHIMINH']
# LATTE_FOREIGN_HOCHIMINHVIP = snapshot['LATTE_FOREIGN_HOCHIMINHVIP']
# LATTE_FOREIGN_LAOPAKEE = snapshot['LATTE_FOREIGN_LAOPAKEE']
# LATTE_FOREIGN_LAORSP = snapshot['LATTE_FOREIGN_LAORSP']
# LATTE_FOREIGN_LAOS = snapshot['LATTE_FOREIGN_LAOS']
# LATTE_FOREIGN_LAOUNITY = snapshot['LATTE_FOREIGN_LAOUNITY']
# LATTE_FOREIGN_MALAY = snapshot['LATTE_FOREIGN_MALAY']

# LATTE_FOREIGN = [LATTE_FOREIGN_HANOI,LATTE_FOREIGN_HANOIEXTRA,LATTE_FOREIGN_HANOIVIP,LATTE_FOREIGN_HOCHIMINH,LATTE_FOREIGN_HOCHIMINHVIP,LATTE_FOREIGN_LAOPAKEE,LATTE_FOREIGN_LAORSP,LATTE_FOREIGN_LAOS,LATTE_FOREIGN_LAOUNITY,LATTE_FOREIGN_MALAY]

# LATTE_THAI = snapshot['LATTE_THAI']
# LATTE_THAI_BAAC = snapshot['LATTE_THAI_BAAC']
# LATTE_THAI_GSB = snapshot['LATTE_THAI_GSB']

# LATTE_THAI = [LATTE_THAI,LATTE_THAI_BAAC,LATTE_THAI_GSB]

# STOCK_FOREIGN_DAX = snapshot['STOCK_FOREIGN_DAX']
# STOCK_FOREIGN_DOWJONES = snapshot['STOCK_FOREIGN_DOWJONES']
# STOCK_FOREIGN_EGX = snapshot['STOCK_FOREIGN_EGX']
# STOCK_FOREIGN_FTSE = snapshot['STOCK_FOREIGN_FTSE']
# STOCK_FOREIGN_HANGSENG_AFTERNOON = snapshot['STOCK_FOREIGN_HANGSENG_AFTERNOON']
# STOCK_FOREIGN_HANGSENG_MORNING = snapshot['STOCK_FOREIGN_HANGSENG_MORNING']
# STOCK_FOREIGN_KOSPI = snapshot['STOCK_FOREIGN_KOSPI']
# STOCK_FOREIGN_MOEX = snapshot['STOCK_FOREIGN_MOEX']
# STOCK_FOREIGN_SENSEX = snapshot['STOCK_FOREIGN_SENSEX']
# STOCK_FOREIGN_STI = snapshot['STOCK_FOREIGN_STI']
# STOCK_FOREIGN_NIKKEI_AFTERNOON = snapshot['STOCK_FOREIGN_NIKKEI_AFTERNOON']
# STOCK_FOREIGN_NIKKEI_MORNING = snapshot['STOCK_FOREIGN_NIKKEI_MORNING']
# STOCK_FOREIGN_SZSE_MORNING = snapshot['STOCK_FOREIGN_SZSE_MORNING']
# STOCK_FOREIGN_SZSE_AFTERNOON = snapshot['STOCK_FOREIGN_SZSE_AFTERNOON']
# STOCK_FOREIGN_TWSE = snapshot['STOCK_FOREIGN_TWSE']
# STOCK_THAI_EVENING = snapshot['STOCK_THAI_EVENING']

# STOCK_FOREIGN= [STOCK_FOREIGN_DAX,STOCK_FOREIGN_DOWJONES,STOCK_FOREIGN_EGX,STOCK_FOREIGN_FTSE,STOCK_FOREIGN_HANGSENG_AFTERNOON,STOCK_FOREIGN_HANGSENG_MORNING,STOCK_FOREIGN_KOSPI,STOCK_FOREIGN_MOEX,STOCK_FOREIGN_SENSEX,STOCK_FOREIGN_STI,STOCK_FOREIGN_NIKKEI_AFTERNOON,STOCK_FOREIGN_NIKKEI_MORNING,STOCK_FOREIGN_SZSE_MORNING,STOCK_FOREIGN_SZSE_AFTERNOON,STOCK_FOREIGN_TWSE,STOCK_THAI_EVENING]

# TH_ABBR_WEEKDAYS = ["จ", "อ", "พ", "พฤ", "ศ", "ส", "อา"]
# TH_FULL_WEEKDAYS = [
#     "วันจันทร์",
#     "วันอังคาร",
#     "วันพุธ",
#     "วันพฤหัสบดี",
#     "วันศุกร์",
#     "วันเสาร์",
#     "วันอาทิตย์",
# ]

# TH_ABBR_MONTHS = [
#     "ม.ค.",
#     "ก.พ.",
#     "มี.ค.",
#     "เม.ย.",
#     "พ.ค.",
#     "มิ.ย.",
#     "ก.ค.",
#     "ส.ค.",
#     "ก.ย.",
#     "ต.ค.",
#     "พ.ย.",
#     "ธ.ค.",
# ]
# TH_FULL_MONTHS = [
#     "มกราคม",
#     "กุมภาพันธ์",
#     "มีนาคม",
#     "เมษายน",
#     "พฤษภาคม",
#     "มิถุนายน",
#     "กรกฎาคม",
#     "สิงหาคม",
#     "กันยายน",
#     "ตุลาคม",
#     "พฤศจิกายน",
#     "ธันวาคม",
# ]

# DLlotto = [
#   {
#     "lottotype": "LATTE_THAI_BAAC",
#     "lottoimg": "https://huaynaka.com/wp-content/uploads/2022/03/BOX_06_%E0%B8%98%E0%B8%81%E0%B8%AA.png",
#     "lottoname": "สลากออมสิน",
#   },
#   {
#     "lottotype": "LATTE_THAI_GSB",
#     "lottoimg": "https://huaynaka.com/wp-content/uploads/2022/03/BOX_06_%E0%B8%AD%E0%B8%AD%E0%B8%A1%E0%B8%AA%E0%B8%B4%E0%B8%99.png",
#     "lottoname": "สลากออมสิน",
#   },
#   {
#     "lottotype": "LATTE_THAI",
#     "lottoimg": "https://tang.huaynaka.com/img/th.76fca72f.svg",
#     "lottoname": "รัฐบาล",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_DAX",
#     "lottoimg": "https://tang.huaynaka.com/img/de.3e726c2b.svg",
#     "lottoname": "หุ้นเยอรมัน",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_DOWJONES",
#     "lottoimg": "https://tang.huaynaka.com/img/us.ae656592.svg",
#     "lottoname": "หุ้นดาวโจนส์",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_EGX",
#     "lottoimg": "https://tang.huaynaka.com/img/eg.6b83ab95.svg",
#     "lottoname": "หุ้นอียิปต์",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_FTSE",
#     "lottoimg": "https://tang.huaynaka.com/img/gb.d3ddd602.svg",
#     "lottoname": "หุ้นอังกฤษ",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_HANGSENG_AFTERNOON",
#     "lottoimg": "https://tang.huaynaka.com/img/hk.06803e0e.svg",
#     "lottoname": "หุ้นฮั่งเส็ง บ่าย",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_HANGSENG_MORNING",
#     "lottoimg": "https://tang.huaynaka.com/img/hk.06803e0e.svg",
#     "lottoname": "หุ้นฮั่งเส็ง เช้า",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_KOSPI",
#     "lottoimg": "https://tang.huaynaka.com/img/kr.eb55e63b.svg",
#     "lottoname": "หุ้นเกาหลี",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_MOEX",
#     "lottoimg": "https://tang.huaynaka.com/img/ru.0cacf46e.svg",
#     "lottoname": "หุ้นรัสเซีย",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_NIKKEI_AFTERNOON",
#     "lottoimg": "https://tang.huaynaka.com/img/jp.99bcc1d7.svg",
#     "lottoname": "หุ้นนิเคอิ บ่าย",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_NIKKEI_MORNING",
#     "lottoimg": "https://tang.huaynaka.com/img/jp.99bcc1d7.svg",
#     "lottoname": "หุ้นนิเคอิ เช้า",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_SENSEX",
#     "lottoimg": "https://tang.huaynaka.com/img/in.e4ab7bd0.svg",
#     "lottoname": "หุ้นอินเดีย",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_STI",
#     "lottoimg": "https://tang.huaynaka.com/img/sg.199f925b.svg",
#     "lottoname": "หุ้นสิงคโปร์",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_SZSE_AFTERNOON",
#     "lottoimg": "https://tang.huaynaka.com/img/cn.02c229de.svg",
#     "lottoname": "หุ้นจีน บ่าย",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_SZSE_MORNING",
#     "lottoimg": "https://tang.huaynaka.com/img/cn.02c229de.svg",
#     "lottoname": "หุ้นจีน เช้า",
#   },
#   {
#     "lottotype": "STOCK_FOREIGN_TWSE",
#     "lottoimg": "https://tang.huaynaka.com/img/hk.06803e0e.svg",
#     "lottoname": "หุ้นไต้หวัน",
#   },
#   {
#     "lottotype": "STOCK_THAI_EVENING",
#     "lottoimg": "https://tang.huaynaka.com/img/th.76fca72f.svg",
#     "lottoname": "หุ้นไทย เย็น",
#   },
#   {
#     "lottotype": "KIWI_05",
#     "lottoname": "หวยยี่กี 5นาที",
#     "lottoimg": "https://tang.huaynaka.com/img/type-yk05.918793ad.png",
#   },
#   {
#     "lottotype": "KIWI_10",
#     "lottoname": "หวยยี่กี 10นาที",
#     "lottoimg": "https://tang.huaynaka.com/img/type-yk10.4f035b4b.png",
#   },
#   {
#     "lottotype": "KIWI_15",
#     "lottoname": "หวยยี่กี 15นาที",
#     "lottoimg": "https://tang.huaynaka.com/img/type-yk15.e3ba21dd.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_HANOI",
#     "lottoname": "หวยฮานอย",
#     "lottoimg": "https://i.imgur.com/TX4BD4c.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_HANOIVIP",
#     "lottoname": "หวยฮานอยวีไอพี",
#     "lottoimg": "https://i.imgur.com/TX4BD4c.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_HANOIEXTRA",
#     "lottoname": "หวยฮานอยเอ็กตร้า",
#     "lottoimg": "https://i.imgur.com/TX4BD4c.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_HOCHIMINH",
#     "lottoname": "หวยโฮจิมินห์",
#     "lottoimg": "https://i.imgur.com/TX4BD4c.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_HOCHIMINHVIP",
#     "lottoname": "หวยโฮจิมินห์วีไอพี",
#     "lottoimg": "https://i.imgur.com/TX4BD4c.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_LAOPAKEE",
#     "lottoname": "หวยลาวปากเซ",
#     "lottoimg": "https://i.imgur.com/n8GgyKP.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_LAORSP",
#     "lottoname": "หวยลาวสัมพันธ์",
#     "lottoimg": "https://i.imgur.com/n8GgyKP.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_LAOS",
#     "lottoname": "หวยลาว",
#     "lottoimg": "https://i.imgur.com/n8GgyKP.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_LAOUNITY",
#     "lottoname": "หวยลาวภาคี",
#     "lottoimg": "https://i.imgur.com/n8GgyKP.png",
#   },
#   {
#     "lottotype": "LATTE_FOREIGN_MALAY",
#     "lottoname": "หวยมาเลย์",
#     "lottoimg": "https://i.imgur.com/F7NGm3J.png",
#   },
#   {
#     "lottotype": "LATTE_THAI",
#     "lottoname": "หวยรัฐบาล",
#     "lottoimg": "https://i.imgur.com/PSmeCfO.png",
#   },
#   {
#     "lottotype": "LATTE_THAI_BAAC",
#     "lottoname": "หวยธกส",
#     "lottoimg": "https://i.imgur.com/1HqxaYp.png",
#   },
#   {
#     "lottotype": "LATTE_THAI_GSB",
#     "lottoname": "หวยออมสิน",
#     "lottoimg": "https://i.imgur.com/6LGpZpw.png",
#   },
# ];




# FLEXFOREIGNS = []
# for FOREIGN in LATTE_FOREIGN:
#     for FOREIG in FOREIGN:
#         if FOREIG['results'][0]['digit'] != "-":
#             #k = len(FOREIG)
#             #print(" "+FOREIG['display_date'][6:8]+" "+FOREIG['display_date'][4:6]+" "+FOREIG['display_date'][0:4])
#             LOreDA = list(filter(lambda x: x['lottotype']==FOREIG['sub_type'], DLlotto))[0]
#             TEMFLEXFLEXFOREIGN={"type": "bubble", "size": "mega", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+LOreDA['lottoimg'], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+LOreDA['lottoname'], "size": "lg", "wrap": True},{"type": "text", "text": FOREIG['display_date'][6:8]+" "+FOREIG['display_date'][4:6]+" "+FOREIG['display_date'][0:4], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+FOREIG['results'][0]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+FOREIG['results'][1]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+FOREIG['results'][2]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover"}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
#             FLEXFOREIGNS.append(TEMFLEXFLEXFOREIGN)


# FLEXSTOCKFOREIGN = []
# for STOCKFOREIGN in STOCK_FOREIGN:
#     for STOCKFORE in STOCKFOREIGN:
#         if STOCKFORE['results'][0]['digit'] != "-":
#             #k = len(STOCKFORE)
#             #print(k)
#             LOreDA = list(filter(lambda x: x['lottotype']==STOCKFORE['sub_type'], DLlotto))[0]
#             TEMFLEXFLEXSTOCKFORE={"type": "bubble", "size": "mega", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+LOreDA['lottoimg'], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+LOreDA['lottoname'], "size": "lg", "wrap": True},{"type": "text", "text": STOCKFORE['display_date'][6:8]+" "+STOCKFORE['display_date'][4:6]+" "+STOCKFORE['display_date'][0:4], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+STOCKFORE['results'][0]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+STOCKFORE['results'][1]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+STOCKFORE['results'][2]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover"}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
#             FLEXSTOCKFOREIGN.append(TEMFLEXFLEXSTOCKFORE)



# def FLEXTIME(type):
#     print(type)
#     dataSET = snapshot[type][0]
#     LOreDA = list(filter(lambda x: x['lottotype']==dataSET['sub_type'], DLlotto))[0]
#     FLEXTIMEX={"type": "bubble", "size": "mega", "header":{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+random.choice(poster), "size": "full", "aspectRatio": "100:50", "aspectMode": "cover", "animated": True, "align": "center", "gravity": "center", "margin": "none"}], "spacing": "none", "margin": "none", "offsetStart": "0px", "paddingAll": "0px"}, "body":{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": ""+LOreDA['lottoimg'], "size": "full", "align": "center", "aspectRatio": "1:1", "aspectMode": "cover"}], "cornerRadius": "100px", "width": "50px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+LOreDA['lottoname'], "size": "lg", "wrap": True},{"type": "text", "text": STOCKFORE['display_date'][6:8]+" "+STOCKFORE['display_date'][4:6]+" "+STOCKFORE['display_date'][0:4], "size": "xs", "weight": "bold", "color": "#DB2316cc"}]}], "spacing": "lg", "alignItems": "center"},{"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "3ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": []},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+dataSET['results'][0]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "xs"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวบน", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderWidth": "1px", "borderColor": "#BD9B51"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+dataSET['results'][1]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": "2ตัวล่าง", "size": "xs", "align": "center", "weight": "bold", "color": "#FFFFFF"}], "backgroundColor": "#A07C00", "paddingAll": "2px", "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "1px"},{"type": "box", "layout": "vertical", "contents": [{"type": "text", "text": ""+dataSET['results'][2]['digit'], "align": "center", "weight": "bold", "size": "3xl", "gravity": "center"}], "height": "50px", "backgroundColor": "#FFFFFFcc", "cornerRadius": "5px", "justifyContent": "center", "borderWidth": "1px", "borderColor": "#BD9B51"}], "spacing": "sm"}], "margin": "lg", "spacing": "sm"},{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "box", "layout": "vertical", "contents": [{"type": "image", "url": "https://huaynaga.info/wp-content/uploads/2021/07/banner-naka-250364-allnew_optimized.jpg", "size": "full", "aspectRatio": "100:40", "aspectMode": "cover"}], "cornerRadius": "5px", "borderColor": "#BD9B51", "borderWidth": "2px"}], "paddingAll": "0px"}], "paddingAll": "0px", "margin": "lg"}], "background":{"type": "linearGradient", "angle": "120deg", "startColor": "#ECDF8C", "endColor": "#C3AA66", "centerColor": "#ECDF8C"}}, "styles":{"body":{"backgroundColor": "#EBDE8A"}}}
#     return FLEXTIMEX



# def FLEXSTOCKGN():
#     SXTEMFLEXFSTOCKGN = {"type": "carousel", "contents": FLEXSTOCKFOREIGN}
#     #print(SXTEMFLEXFSTOCKGN)
#     return SXTEMFLEXFSTOCKGN

# def FLEXFOREIGN():
#     SXTEMFLEXFLEXFOREIGN = {"type": "carousel", "contents": FLEXFOREIGNS}
#     #print(SXTEMFLEXFLEXFOREIGN)
#     return SXTEMFLEXFLEXFOREIGN

