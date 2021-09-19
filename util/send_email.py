#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
class Send_email():
    def __init__(self):
        pass
    global send_user
    global email_host
    global password
    email_host="smtp.163.com"
    password="123456abcd" #进入邮箱开启smtp/pop3服务，获取授权码，需要使用授权码登录才能发送，不是邮箱密码
    send_user = "yanshunhua163@163.com"

    def send_mail(self,user_list,sub,content,file_names):

        msg=MIMEMultipart()

        user="myolse"+"<"+send_user+">"
       # message=MIMEText(content,_subtype='plain',_charset='utf-8')

        msg.attach(MIMEText(content,_subtype='plain',_charset='utf-8'))

        msg['Subject'] = Header(sub,'utf-8')
        msg['From'] = user
        msg['To'] = ";".join(user_list)

        # message['Subject']=sub
        # message['From']=user
        # message['To']=";".join(user_list)
       # server=smtplib.SMTP(email_host,25)
        # 附件:附件名称用英文
        for file_name in file_names:
            att = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment;filename="%s"' % (file_name)
            msg.attach(att)


        server=smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)

        server.sendmail(user,user_list,msg.as_string())
        server.close()
if __name__=="__main__":
        sen=Send_email()
        user_list1=['yanshunhua163@163.com']
        sub='这是个测试邮件'
        content="这是我们的一封测试邮件"
        file_names = ["../report/TestReport2.html"]
        sen.send_mail(user_list1,sub,content,file_names)