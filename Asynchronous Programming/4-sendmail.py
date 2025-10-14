import smtplib
import asyncio

# async def send_mail():
#     content = "Hello World"
#     mail = smtplib.SMTP('smtp.gmail.com',port=535)
#     mail.ehlo()
#     mail.starttls()
#     sender = '22it256.harsh.lunagariya@vvpedulink.ac.in'
#     recipient = 'harshlunagariya15@gmail.com'
#     mail.login(user='22it256.harsh.lunagariya@vvpedulink.ac.in',password='qaz_plm@256')
#     header='To:'+recipient+'\n'+'From:' \
#     +sender+'\n'+'subject: testmail\n'
#     content = header+content
#     mail.sendmail(sender,recipient,content)
#     mail.close()

# async def main():
#     asyncio.create_task(send_mail())
#     print('doing other task')

# asyncio.run(main())

from email.message import EmailMessage

sender = '22it256.harsh.lunagariya@vvpedulink.ac.in'
recipient = 'harshlunagariya15@gmail.com'
password='qaz_plm@256'

msg = EmailMessage()
msg['Subject'] = "Test"
msg['From'] = sender
msg['To'] = recipient
msg.set_content("Hello from Python!")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)   # likely to fail if Google blocks the login
    smtp.send_message(msg)
    print("Sent")

