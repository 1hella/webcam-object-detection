import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("RECEIVER_EMAIL")


def send_email(image_path):
    print('send email function started')
    email_message = EmailMessage()
    email_message['Subject'] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(USERNAME, PASSWORD)
    gmail.sendmail(USERNAME, RECEIVER, email_message.as_string())
    gmail.quit()
    print('send email function ended')

if __name__ == "__main__":
    send_email("images/26.png")