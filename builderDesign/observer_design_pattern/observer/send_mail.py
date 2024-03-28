import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(receiver_email, subject, message_body):
    sender_email = "your_email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587  # Port for TLS
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = 'md.irfan7839@gmail.com'
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add message body
    message.attach(MIMEText(message_body, "plain"))

    # Connect to SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_username, smtp_password)  # Login to SMTP server
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send email
    print("Email sent successfully!")


# Example usage


send_mail(sender_email, receiver_email, subject, message_body, smtp_server, smtp_port, smtp_username, smtp_password)
