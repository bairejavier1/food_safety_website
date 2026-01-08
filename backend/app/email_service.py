import smtplib
from email.message import EmailMessage
from app.config import GMAIL_USER, GMAIL_PASSWORD, RECEIVER_EMAIL

def send_email(name: str, phone: str):
    msg = EmailMessage()
    msg["Subject"] = "New Food Safety Service Request"
    msg["From"] = GMAIL_USER
    msg["To"] = RECEIVER_EMAIL

    msg.set_content(
        f"""
New service request received:

Name: {name}
Phone: {phone}

Please call the customer back.
        """
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)
