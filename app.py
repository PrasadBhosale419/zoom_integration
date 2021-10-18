from flask import Flask,jsonify,request
from flask_restful import Resource, Api, reqparse, abort
import smtplib
from email.message import EmailMessage
from datetime import datetime
import time
import requests

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    #print("Hello")
    url = "https://api.zoom.us/v2/users/me/meetings"
    title = request.form.get("title")
    # parser = reqparse.RequestParser()
    # title = str(parser.add_argument('title', type=str))
    print(title)
    payload="{\r\n  \"topic\": \""+title+"\",\r\n  \"type\":2,\r\n  \"start_time\": \"2021-10-14T12:10:10Z\",\r\n  \"duration\":\"3\",\r\n  \"settings\":{\r\n   \"host_video\":true,\r\n   \"participant_video\":true,\r\n   \"join_before_host\":true,\r\n   \"mute_upon_entry\":\"true\",\r\n   \"watermark\": \"true\",\r\n   \"audio\": \"voip\",\r\n   \"auto_recording\": \"cloud\"\r\n     } \r\n  \r\n }"

    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiJjNTUxMTE3YS1jNzAwLTQ2MTUtOThkZi1hZDg5YTAxN2UwZDUifQ.eyJ2ZXIiOjcsImF1aWQiOiIxZGQ2ZGUxMDU1MDZkMmNjMjZiYTYxYjNjMGYwMWM5MiIsImNvZGUiOiJVNWt1dUR6MmRRX2xxSE84RVRHUXh1WW93c1l4cmlIR2ciLCJpc3MiOiJ6bTpjaWQ6OVN4MXFva3ZSV0J5czgzZWtsdzdnIiwiZ25vIjowLCJ0eXBlIjowLCJ0aWQiOjAsImF1ZCI6Imh0dHBzOi8vb2F1dGguem9vbS51cyIsInVpZCI6ImxxSE84RVRHUXh1WW93c1l4cmlIR2ciLCJuYmYiOjE2MzQ1NTE4OTQsImV4cCI6MTYzNDU1NTQ5NCwiaWF0IjoxNjM0NTUxODk0LCJhaWQiOiItNHlWVGdxM1JWYWVUa1ZPLTlMeVF3IiwianRpIjoiNjM5ZDk4N2ItNjdlOS00ODlkLWIyOWYtYjIxZTQ3MDM3MzhlIn0.6E2IFTeBrU6e8_NGlC2Hh2fqlppAnEEJMs4N_VDrg6cmUAeQ7UBlE7RZBViMNMKA9omMcWOSoQlKxACkUC8leQ',
    'Content-Type': 'application/json',
    'Cookie': '_zm_mtk_guid=ed9e7ba566db473a86c5ffc5a556c5ea; _zm_lang=en-US; _zm_currency=INR; _zm_login_acctype=2; cred=82784A7334D2A6B7CB0BB2DE60D60C21; _zm_ctaid=jH5TNxXPQMqjx4cNKw368Q.1634551818057.c07de004b201de9018ff5aeff716f99e; _zm_chtaid=853; TS01da2a01=01141133616eae0f6e71e3610b63dac259f6d2ae8896c64f48a94982508db61efe4c6b8b291ab8bef34f9bc67a6386337c7846c226; TS01aed67e=01141133616eae0f6e71e3610b63dac259f6d2ae8896c64f48a94982508db61efe4c6b8b291ab8bef34f9bc67a6386337c7846c226'
    }
    #print("Hello")
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.text


# def hello_world():
#     msg = EmailMessage()
#     msg['Subject']=str(request.args.get('subject'))
#     msg['From']="hackathonviit@gmail.com"
#     msg['To']=str(request.args.get('emailid'))
#     print(str(request.args.get('emailid')))
#     #cc="ameybobade1103@gmail.com,pmacoe.it@gmail.com"
#     msg['Cc'] = (str(request.args.get('cc'))).split(',')
#     msg['Bcc'] = (str(request.args.get('bcc'))).split(',')
#     # msg['Bcc'] = bcc.split(',')
#     msg.set_content(str(request.args.get('message')))
#
#     StartYear = request.args.get('syear')
#     StartMonth = request.args.get('smonth')
#     StartDate = request.args.get('sdate')
#     StartTimehour = request.args.get('shour')
#     StartTimemin = request.args.get('smin')
#     EndYear = request.args.get('eyear')
#     EndMonth = request.args.get('emonth')
#     EndDate = request.args.get('edate')
#     EndTimehour = request.args.get('ehour')
#     EndTimemin = request.args.get('emin')
#     Summary = request.args.get('summary')
#     Description = request.args.get('description')
#     string="BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\nDTSTART:"+str(StartYear)+str(StartMonth)+str(StartDate)+"T"+str(StartTimehour)+str(StartTimemin)+"000\nDTEND:"+str(EndYear)+str(EndMonth)+str(EndDate)+"T"+str(EndTimehour)+str(EndTimemin)+"000\nUID:ameybobade@gmail.com\nSUMMARY:"+Summary+"\nDESCRIPTION:"+Description+"\nEND:VEVENT\nEND:VCALENDAR"
#
#     with open('invite.ics', 'w') as my_file:
#         my_file.writelines(string)
#
#
#     file = open('invite.ics', 'r')
#     if file:
#         file_data = file.read()
#         file_name = file.name
#         print(file_name)
#         # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
#         msg.add_attachment(file_data, subtype='octet-stream', filename=file_name)
#
#     try:
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login("hackathonviit@gmail.com", "viithackathon")
#             smtp.send_message(msg)
#         result={
#             "Status" : "Sent",
#             "Time" : time.asctime( time.localtime(time.time()) )
#         }
#
#     except:
#         result={
#             "Status" : "Error in Authentication",
#             "Time" : time.asctime( time.localtime(time.time()) )
#         }
#     return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(debug=True)

# file = open('sbc.txt', 'r')
# This will print every line one by one in the file
# for each in file:
#     print (each)
