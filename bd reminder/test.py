import smtplib

gmailuser = 'jasonchae1404@gmail.com'
password =


sent_from = 'you@gmail.com'
to = [gmailuser, 'jasonchae1404@gmail.com']
subject = 'OMG Super Important Message'
body = "Hey, what's up?\n\n- You"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmailuser, password)
    server.sendmail(sent_from, to, email_text)
    server.close()


    print('Email sent!')
except:
    print('Something went wrong...')