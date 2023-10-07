import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# def registration_confirmation_mail(user_email, message):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     try:
#         # msg = EmailMessage()
#         msg = MIMEMultipart("alternatives")
#         # msg.set_content(message)
#         msg['Subject'] = 'Welcome to The Great Affiliaters | Registration verification'
#         msg['From'] = "great.affiliators@gmail.com"
#         msg['To'] = user_email
#         msg.attach(MIMEMultipart(message, "html"))
#         server.login('great.affiliators@gmail.com', 'poygiytxcaypmisu')
#         print("login ho gaya")
#         server.send_message(msg)
#         return True
#     except Exception as e:
#         print(e)
#         print("Mail not sent")
#         return False

def registration_confirmation_mail(user_email, message):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'great.affiliators@gmail.com'
    sender_password = 'poygiytxcaypmisu'
    subject = 'Welcome to The Great Affiliaters | Registration verification'

    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user_email
        msg['Subject'] = subject

        # Add HTML content to the message body
        body = MIMEText(message, 'html')
        msg.attach(body)

        # Create SMTP session for sending the email
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            print("login ho gaya")
            server.send_message(msg)
        
        return True

    except Exception as e:
        print(e)
        return False