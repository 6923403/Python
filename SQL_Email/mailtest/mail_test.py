import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
    try:
        print(1)
        try:
            print(2)
            from_addr = "5435@163.com"
            passwd = "NRRTICETCSIPZGWH"
            mailhost = "smtp.163.com"
            to_addr = "6923403@qq.com"

            wy_mail = smtplib.SMTP()  # 建立SMTP对象
            wy_mail.connect(mailhost, 25)  # 25为SMTP常用端口
            wy_mail.login(from_addr, passwd)  # 登录邮箱


            """
            content = "恭喜你抢购成功 \n" + "用户名：{} \n".format(self.get_username()) + "当前工作目录{}".format(os.getcwd()) + \
                      "抢购成功，订单号:{}, 总价:{}, 电脑端付款链接:{} \n".format(order_id, total_money, pay_url)
            """
            content = "抢购成功 \n" + "用户名: 123444 \n" + "目录: {}".format(os.getcwd())
            # 拼接题目字符串
            subject = time.strftime("%Y-%m-%d_%H_%M", time.localtime(time.time())) + "今日Maotai"

            # 加工邮件message格式
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['From'] = "Name1<5435@163.com>"
            msg['To'] = "Name2<6923403@qq.com>"
            msg['subject'] = Header(subject, 'utf-8')

            try:
                wy_mail.sendmail(from_addr, to_addr, msg.as_string())
                print('邮件发送成功')
            except Exception as e:
                print(str(e))
            wy_mail.quit()
        except:
            print(2)
    except:
        print(1)

