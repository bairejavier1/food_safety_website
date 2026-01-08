import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .config import settings
from .models import ServiceRequest


def send_service_request_email(request: ServiceRequest) -> None:
    """
    Sends an email notification to the service provider
    when a new service request is submitted.
    """
    if not settings.EMAIL_SENDER or not settings.EMAIL_PASSWORD:
        raise RuntimeError("Email sender or password not configured in environment variables")

    sender_email = settings.EMAIL_SENDER
    recipient_email = settings.EMAIL_RECIPIENT

    subject = "New Food Safety Service Request"
    body = (
        f"A new service request has been submitted:\n\n"
        f"Name: {request.name}\n"
        f"Phone: {request.phone}\n"
        f"Message: {request.message or 'No additional message provided.'}\n"
    )

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
        server.send_message(msg)
