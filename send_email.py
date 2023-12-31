# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail:
    def __init__(self):
        # 第三方 SMTP 服务

        self.mail_host = "smtp.qq.com"  # 设置服务器:这个是qq邮箱服务器，复制就行
        self.mail_pass = "xbgcbidrndzibeei"  # 刚才我们获取的授权码
        self.sender = '773916295@qq.com'  # 你的邮箱地址
        self.receivers = []  # 收件人的邮箱地址，可设置为你的QQ邮箱或者其他邮箱，可多个
        self.mail_content = ''

    def send(self,content):

        # content = self.mail_content  # 邮件内容
        # content += '嘟嘟天气小提醒：\r\n'
        # content += '明 天 是 ： '+list[0][0]['date']+'\r\n'
        # content += '天{}{}气：'.format(chr(12288),chr(12288))+list[0][0]['weatherText']+'\r\n'
        # content += '白{}{}天：'.format(chr(12288),chr(12288))+list[0][0]['weatherWind']['windDirectionDay']+list[0][0]['weatherWind']['windPowerDay']+'\r\n'
        # content += '空气质量：'+list[0][0]['weatherPm25']+'\r\n'
        # content += '气{}{}温：'.format(chr(12288),chr(12288))+list[0][2]['temperature']+'——'+list[0][1]['temperature']+'\r\n'
        message = MIMEText(content, 'plain', 'utf-8')
        # content = '<html><body>'
        # content += '<p>嘟嘟天气小提醒:</p>'
        # content += '<p>明 天 是:<var>list[0][0]['date']</var></p>'
        # content += '<img src="cid:imageid" alt="imageid">'
        # content += '</body></html>'
        # content += '<p>再见</p>'

        # # 邮件内容 文本+图片
        # content = '<html><body>'
        # content += '<p>你好：<br />这是一个测试邮件...</p>'
        # content += '<img src="cid:imageid" alt="imageid">'
        # content += '</body></html>'
        # content += '<p>再见</p>'
        # message.attach(MIMEText(content, 'html', 'utf-8'))

        # image_data = open(r'C:/Users/29000/Desktop/5SA[)5W%RR3BJ2FKL9J0FKF.jpg', 'rb')  # 二进制读取图片
        # message_image = MIMEImage(image_data.read(), _subtype='octet-stream')  # 设置读取获取的二进制数据
        # image_data.close()  # 关闭刚才打开的文件
        # message_image.add_header('Content-ID', 'imageid')  # imageid 与上边html中的imageid 对应
        # message.attach(message_image)  # 添加图片文件到邮件内容当中去

        # # 添加附件
        # attachment_name = '测试附件.docx'
        # attachment = f'C:/Users/29000/Desktop/{attachment_name}'
        # message_file = MIMEApplication(open(attachment, 'rb').read(), _subtype='octet-stream')
        # message_file.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        # message.attach(message_file)

        message['From'] = Header("'=?UTF-8?B?5Zif5Zif' <{}>".format(self.sender)) # 发件人名称
        message['To'] = Header("'=?UTF-8?B?5ZW+5ZW+' <{}>".format(self.receivers))  # 收件人名称

        subject = '明日天气'  # 发送的主题，可自由填写
        # subject = self.mail_content
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            # print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败',self.receivers,e)

def send_mail(content,re_mail):
    mail = Mail()
    if re_mail != '':
        mail.receivers = [re_mail]
    # mail.mail_content=content
    # mail.mail_content = content
    mail.send(content)

if __name__ == '__main__':
    content = 'hanshu ceshi'
    send_mail(content)