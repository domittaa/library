import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


def send_email(message, receiver_email="test@gmail.com"):
    print(f"Sending email with message: {message}")
    password = os.getenv("MAIL_PASSWORD")
    email = os.getenv("MAIL_ADDRESS")

    msg = EmailMessage()
    msg["Subject"] = "Order expiration notification"
    msg["From"] = email
    msg["To"] = receiver_email
    msg.set_content(message)

    smpt_server = "smtp.gmail.com"
    smpt_port = 587

    try:
        with smtplib.SMTP(smpt_server, smpt_port) as server:
            server.starttls()
            server.login(email, password)
            server.send_message(msg)
        print("Email sent!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


if __name__ == "__main__":
    send_email("test@gmail.com", "This is a test")
