from flask import Flask, request,abort
import json
import requests
import mysql.connector
import sys
import mysql.connector 

from Project.config import *   # folder Project file config
from Project.flextimetable import *   # folder Project file flextimetable
from Project.flexexam import *   # folder Project file flexexamtable
from Project.grades import *  # folder Project file grades
from Project.test import *   # folder Project file test
from Project.regis import *  # folder Project file regis
from Project.payment import *  # folder Project file payment
from Project.contact import *  # folder Project file contact

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageSendMessage, StickerSendMessage, AudioSendMessage, FlexSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)

# mydb = mysql.connector.connect(
#   host='database',
#   user='user',
#   password='password',
#   database='db',
#   port='3306'
# )
# mycursor = mydb.cursor()
# # print(mycursor)

app = Flask(__name__)

line_bot_api = LineBotApi(channel_access_token)

@app.route('/')
def index():

  return "reg line chat bot"

#   Webhook

@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    if request.method == 'POST' :
      payload = request.json
      # print(payload)
      if payload != None : 
        # print(request.json)
        payload = request.json
        # print(payload)
        message = payload['events'][0]['message']['text']
        print(message)
      
        json_line = request.get_json(force=False,cache=False)
        json_line = json.dumps(json_line) # convert python dict to json string
        decoded = json.loads(json_line)  # convert json string to python dict
        # print(decoded)
#         userId = payload['events'][0]['source']['userId']
#         sql = "SELECT line_userID FROM studentaccount WHERE line_userID = %s "
#         val = (userId,)
#         mycursor.execute(sql,val)
#         myresult = mycursor.fetchall()
#         print(len(myresult))

#         if len(myresult) != 0 :
        
        # time table test
#             if "สอบถามตารางเรียน / class schedule" in message:
#                 sql = "SELECT  s.studentcode,s.studentname,s.studentsurname,s.prefixname,s.line_userID,t.acadyear,t.semester,t.coursename,t.coursecode,t.studytype,TIME_FORMAT(t.timefrom, \"%H:%i\"),TIME_FORMAT(t.timeto, \"%H:%i\"),t.sec,t.room,t.dayID,w.dayname FROM studentaccount s , timetable t , weekday w WHERE s.studentID = t.studentID and s.line_userID = %s and t.dayID = w.dayID order by t.dayID ,t.timefrom ,t.coursecode"
#                 val = (userId,)
#                 mycursor.execute(sql,val)
#                 myresult = mycursor.fetchall()
#                 # print(myresult)
#                 table = []

#                 for i in myresult:
#                     table.append(i)
                    
#                 flex = flex_timetable(table)
#                 print(flex)
#                 flexdict = json.loads(flex)     # convert json string to python dict
#                 print(flexdict)
#                 replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flex)
#                 #  print(replyObj)
                    
        
#         # time exam test
#             if "สอบถามตารางสอบ / exam schedule" in message:
#                 sql = "select  s.studentcode,s.studentname,s.studentsurname,s.prefixname,s.line_userID,x.acadyear,x.semester,x.coursecode,x.coursename,TIME_FORMAT(x.timefrom, \"%H:%i\"),TIME_FORMAT(x.timeto, \"%H:%i\"),x.datetimes,x.sec,x.room,x.seatnumber,x.examtype from studentaccount s , timeexam x where s.studentID = x.studentID and s.line_userID = %s order by x.datetimes ,x.timefrom"
#                 val = (userId,)
#                 mycursor.execute(sql,val)
#                 myresult = mycursor.fetchall()
#                 # print(myresult)
#                 table = []

#                 for i in myresult:
#                     table.append(i)
                    
#                 flex = flex_timeexam(table)
#                 print(flex)
#                 flexdict = json.loads(flex)     # convert json string to python dict
#                 print(flexdict)
#                 replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flexdict)
#             #   print(replyObj)

#             # grade table test
#             if "สอบถามผลการศึกษา / grade result" in message:
#                 sql = "select s.studentcode, s.prefixname, s.studentname, s.studentsurname, s.line_userID, g.semester, g.acadyear, g.coursecode, g.coursename, g.credit, g.CA, g.CAA, g.grade, g.GPA, g.GPAX from studentaccount s, grades g where s.studentID = g.studentID and s.line_userID = %s order by g.semester, g.coursecode"
#                 val = (userId,)
#                 mycursor.execute(sql,val)
#                 myresult = mycursor.fetchall()
#                 # print(myresult)
#                 table = []
                
#                 for i in myresult:
#                     table.append(i)
                    
#                 flex = flex_grades(table)
#                 print(flex)
#                 flexdict = json.loads(flex)     # convert json string to python dict
#                 print(flexdict)
#                 replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flexdict)
#             #   print(replyObj)

#         else :
#             replyObj = TextSendMessage(text='please sing up https://reg7.nu.ac.th/registrar/home.asp?lang=1')
#             print("please sign up")            

#         if "ระบบทะเบียนออนไลน์ / registration" in message :
#             flex = flex_regismenu()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='การลงทะเบียนออนไลน์', contents=flexdict)
#             # print(replyObj)
        
#         if "เตรียมพร้อมก่อนการลงทะเบียน" in message :
#             flex = flex_regisAnswer1()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict                print(flexdict)
#             replyObj = FlexSendMessage(alt_text='เตรียมพร้อมก่อนการลงทะเบียน', contents=flexdict)
#             # print(replyObj)

#         if "ลืมรหัสผ่านเข้าระบบ" in message :
#             flex = flex_regisAnswer2()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='ลืมรหัสผ่านเข้าระบบ', contents=flexdict)
#             # print(replyObj)

#         if "บัตรประจำตัวนิสิตหาย" in message :
#             flex = flex_regisAnswer3()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='บัตรประจำตัวนิสิตหาย', contents=flexdict)
#             # print(replyObj)
                
#         if "เปลี่ยนแปลงข้อมูลส่วนตัว" in message :
#             flex = flex_regisAnswer4()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='เปลี่ยนแปลงข้อมูลส่วนตัว', contents=flexdict)
#             # print(replyObj)
                
#         if "ไม่ได้ลงทะเบียนเรียน/ชำระเงิน" in message :
#             flex = flex_regisAnswer5()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='ไม่ได้ลงทะเบียนเรียน/ชำระเงิน', contents=flexdict)
#             # print(replyObj)

#         if "ติดต่อ" in message :
#             flex = flex_regisAnswer6()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
#             # print(replyObj) 


#         if "การชำระค่าทำเนียมการศึกษา / tuition fee payment" in message : 
#             flex = flex_paymentmenu()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='การชำระค่าทำเนียมการศึกษา', contents=flexdict)
#             # print(replyObj)

#         if "การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน" in message :
#             flex = flex_paymentAnswer1()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน', contents=flexdict)
#             # print(replyObj) 
                
#         if "ช่องทางการชำระเงิน" in message :
#             flex = flex_paymentAnswer2()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='ช่องทางการชำระเงิน', contents=flexdict)
#             # print(replyObj) 
                
#         if "ตรวจสอบสถานะการชำระเงินและพิมพ์ใบเสร็จ" in message :
#             flex = flex_paymentAnswer3()
#             print(flex)
#             flexdict = json.loads(flex)     # convert json string to python dict
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='ตรวจสอบสถานะการชำระเงินและพิมพ์ใบเสร็จ', contents=flexdict)
#             # print(replyObj) 

#         if "ติดต่อเพิ่มเติม / contactmore" in message :
#             flex = contact()
#             print(flex)
#             flexdict = json.loads(flex)
#             print(flexdict)
#             replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
#             # print(replyObj)

        # if "ติดต่อ" in message :
        #         flex = flex_regisAnswer6()
        #         flexdict = json.loads(flex)     # convert json string to python dict
        #         print(flexdict)
        #         replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
                # print(replyObj) 

        no_event = len(decoded['events'])
        
        for i in range(no_event):
            event = decoded['events'][i]
            event_handle(event)
        return '',200

      else :
        print("no request")
        abort(400)

    elif request.method == 'GET':
        return 'this is method get !!!' , 200
    else:
        abort(400)

def event_handle(event):
    # print(event)
    try:
        userId = event['source']['userId'] # get line userid
    except:
        print('error cannot get userId')
        return ''
    try:
        rtoken = event['replyToken'] # get reply token
    except:
        print('error cannot get rtoken')
        return ''
    if 'message' in event.keys():
        try:
            msgType = event["message"]["type"]
            msgId = event["message"]["id"]
        except:
            print('error cannot get msgID, and msgType')
            # sk_id = np.random.randint(1,17)
            # replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
            # line_bot_api.reply_message(rtoken, replyObj)
            return ''
    if msgType == "text":
        msg = str(event["message"]["text"])
        print(msg)
        replyObj = handle_text(msg)
        line_bot_api.reply_message(rtoken, replyObj)
    return ''

from linebot.models import (TextSendMessage,FlexSendMessage)
def handle_text(inpmessage):

#     payload = request.json
#     userId = payload['events'][0]['source']['userId']
#     sql = "SELECT line_userID FROM studentaccount WHERE line_userID = %s "
#     val = (userId,)
#     mycursor.execute(sql,val)
#     myresult = mycursor.fetchall()
#     print(len(myresult))

#     if len(myresult) != 0 :
    if "สอบถามตารางเรียน" in inpmessage:
            flex = flex_timetable()
            
            #   print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flex)
            #   print(replyObj)

            # time exam test
    if "สอบถามตารางสอบ" in inpmessage:
         flex = flex_timeexam()
         #   print(flex)
         flexdict = json.loads(flex)     # convert json string to python dict
         print(flexdict)
         replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flexdict)
         #   print(replyObj)

        # grade table test
    if "สอบถามผลการเรียน" in inpmessage:
       
         flex = flex_grades()
         flexdict = json.loads(flex)     # convert json string to python dict
         print(flexdict)
         replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flexdict)
         #   print(replyObj)

    if "การลงทะเบียนออนไลน์" in inpmessage :
        flex = flex_regismenu()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='การลงทะเบียนออนไลน์', contents=flexdict)
        # print(replyObj)
        
    if "เตรียมพร้อมก่อนการลงทะเบียน" in inpmessage :
        flex = flex_regisAnswer1()
        flexdict = json.loads(flex)     # convert json string to python dict                print(flexdict)
        replyObj = FlexSendMessage(alt_text='เตรียมพร้อมก่อนการลงทะเบียน', contents=flexdict)
        # print(replyObj)

    if "ลืมรหัสผ่านเข้าระบบ" in inpmessage :
        flex = flex_regisAnswer2()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ลืมรหัสผ่านเข้าระบบ', contents=flexdict)
        # print(replyObj)

    if "บัตรประจำตัวนิสิตหาย" in inpmessage :
        flex = flex_regisAnswer3()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='บัตรประจำตัวนิสิตหาย', contents=flexdict)
        # print(replyObj)
                
    if "เปลี่ยนแปลงข้อมูลส่วนตัว" in inpmessage :
        flex = flex_regisAnswer4()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='เปลี่ยนแปลงข้อมูลส่วนตัว', contents=flexdict)
        # print(replyObj)
                
    if "ไม่ได้ลงทะเบียนเรียน/ชำระเงิน" in inpmessage :
        flex = flex_regisAnswer5()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ไม่ได้ลงทะเบียนเรียน/ชำระเงิน', contents=flexdict)
        # print(replyObj)

    if "ติดต่อ" in inpmessage :
        flex = flex_regisAnswer6()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
        # print(replyObj) 


    if "การชำระค่าทำเนียมการศึกษา" in inpmessage : 
        flex = flex_paymentmenu()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='การชำระค่าทำเนียมการศึกษา', contents=flexdict)
        # print(replyObj)

    if "การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน" in inpmessage :
        flex = flex_paymentAnswer1()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน', contents=flexdict)
        # print(replyObj) 
                
    if "ช่องทางการชำระเงิน" in inpmessage :
        flex = flex_paymentAnswer2()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ช่องทางการชำระเงิน', contents=flexdict)
        # print(replyObj) 
                
    if "ตรวจสอบสถานะการชำระเงินและพิมพ์ใบเสร็จ" in inpmessage :
        flex = flex_paymentAnswer3()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ตรวจสอบสถานะการชำระเงินและพิมพ์ใบเสร็จ', contents=flexdict)
        # print(replyObj) 

    if "ติดต่อ" in inpmessage :
        flex = flex_regisAnswer6()
        flexdict = json.loads(flex)     # convert json string to python dict
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
        # print(replyObj) 
    
    if "ติดต่อเพิ่มเติม / contactmore" in inpmessage :
        flex = contact()
        print(flex)
        flexdict = json.loads(flex)
        print(flexdict)
        replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
         # print(replyObj)

    if 'สวัสดี' in inpmessage :
        replyObj = TextSendMessage(text='สวัสดีค่ะ')
  
    if 'hi' in inpmessage :
        replyObj = TextSendMessage(text='hello')

    return replyObj

# def ReplyMessage(Reply_token, TextMassage, Line_Access_Token ):
#   LINE_API = 'https://api.line.me/v2/bot/message/reply'

#   Authorization = 'Bearer {}'.format(Line_Access_Token) # channel_access_token
#   print(Authorization)

#   headers = {
#         'Content-Type': 'application/json; charset=UTF-8',
#         'Authorization':Authorization
#     }
#   data = {
#         "replyToken":Reply_token,
#         "messages":[{
#           "type":"text",
#           "text":TextMassage
#         }]
#   }

#   data = json.dumps(data)
#   r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
#   print(r.text)
  # return 200

# def Reply_Flex(user, flex_message, Line_Acees_Token):
#     LINE_API = "https://api.line.me/v2/bot/message/push"

#     Authorization = 'Bearer {}'.format(Line_Acees_Token)
    
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization':Authorization
#     }
#     data = {
#         "to":str(user),
#         "messages":[{
#             "type": "flex",
#             "altText": "This is a Flex Message",
#             "contents":flex_message
#         }]
#     }
#     data = json.dumps(data) ## dump dict >> Json Object
#     r = requests.post(LINE_API, headers=headers, data=data) 
#     return 200

    
    
    # LINE_API = 'https://api.line.me/v2/bot/message/reply'

    # Authorization = 'Bearer {}'.format(bot_access_key)

    # headers = {'Content-Type': 'application/json; charset=UTF-8',
    # 'Authorization': Authorization}

    # file_data['replyToken'] = reply_token
    # #### dumps file จาก dict ให้เป็น json
    # file_data = json.dumps(file_data)
    # r = requests.post(LINE_API, headers=headers, data=file_data) # ส่งข้อมูล

    # return 200

  # def Reply_Imagemap(user, imagemap_message, Line_Acees_Token):
  #   LINE_API = "https://api.line.me/v2/bot/message/push"
  #   Authorization = 'Bearer {}'.format(Line_Acees_Token)
  #   headers = {
  #       'Content-Type': 'application/json',
  #       'Authorization':Authorization
  #   }
  #   data = {
  #       "to":str(user),
  #       "messages":[{
  #           "type": "imagemap",
  #           "altText": "This is a 'Imagemap",
  #           "contents":flex_message
  #       }]
  #   }
  #   data = json.dumps(data) ## dump dict >> Json Object
  #   r = requests.post(LINE_API, headers=headers, data=data) 
  #   return 200

# if __name__ == '__main__':
#   app.run(debug=True)


