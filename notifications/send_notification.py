import os
import smtplib
import ssl


def send_email(receiver_email, message):
    sender_email = "mentoringprojektbiblioteka@gmail.com"
    port = 465
    password = os.getenv("MAIL_PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smpt.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
