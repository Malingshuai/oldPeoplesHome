# coding:utf-8
"""
目的：发送html文本邮件
作者： 马令帅
修改日期：2017.01.03
"""
import smtplib
from email.mime.text import MIMEText

mailto_list = ["531792735@qq.com"]
mail_host = "smtp.exmail.qq.com"            # 设置服务器
mail_user = "malingshuai@esuizhen.com"      # 用户名
mail_pass = ""                   # 口令
mail_postfix = "esuizhen.com"               # 发件箱的后缀


def send_mail(to_list, sub, reportpath):
    """ to_list：收件人；sub：主题；content：邮件内容"""
    files = open(reportpath, "rb")
    content = ""
    for line in files.readlines():
        # line = line.decode()                                           # python3x版本，需要添加该行
        content = content + line.replace("class='hiddenRow'", "")

    me = "马令帅" + "<" + mail_user + ">"  # "@" + mail_postfix + ">"    # 收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='utf-8')           # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub                                                 # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.set_debuglevel(1)
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception as e:
        print (str(e))
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "TestResult",
                 r'F:\03demo\seleniumPythonDemo\automationDemo\projectName\report\2017_01_03 13_43_02result.html'):
        print (u"发送成功")
    else:
        print (u"发送失败")
