import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('classymatexs@gmail.com','hbdwvogqkdfkypdi')
subject='Hello there'
body='25th ko movie chalte hai!!'
msg="subject:{}\n\n{}".format(subject,body)
listadd=[' karthikeya.peeriga@gmail.com ']
ob.sendmail('classymatexs@gmail.com',listadd,msg)
print("send mail")
ob.quit()
