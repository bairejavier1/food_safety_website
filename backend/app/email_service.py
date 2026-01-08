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

    print("📨 Preparing email...")  # DEBUG LOG

    sender_email = settings.EMAIL_SENDER
    app_password = settings.EMAIL_PASSWORD
    recipient_email = settings.EMAIL_RECIPIENT

    if not sender_email or not app_password:
        raise RuntimeError("Email sender or password missing in .env")

    subject = "New Food Safety Service Request"
    body = (
        f"New service request submitted:\n\n"
        f"Name: {request.name}\n"
        f"Phone: {request.phone}\n"
        f"Message: {request.message or 'No message provided'}\n"
    )

    print("📧 Email body:")
    print(body)

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        print("🔌 Connecting to Gmail SMTP...")
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            print("🔐 Logging in...")
            server.login(sender_email, app_password)
            print("📤 Sending email...")
            server.send_message(msg)
            print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ ERROR sending email:", e)
        raise
