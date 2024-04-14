import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse

def send_results_email(recipient_email, results):
    sender_email = "notescratchonline@gmail.com"
    subject = "Notification!"

    greeting = "Hello!"
    
    html_content = f"""
    <html>
      <body>
        <p>{greeting}</p>
        <p>Here are the results of the scan:</p>
        <ul>
    """

    for result in results:
        icon = "✗" if "true" in result else "✓"
        html_content += f"<li>{icon} {result.split(' ')[0]} is {'not ' if 'true' in result else ''}following social distancing</li>"

    html_content += """
        </ul>
      </body>
    </html>
    """

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    html_part = MIMEText(html_content, "html")
    message.attach(html_part)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587  
    smtp_username = "notescratchonline@gmail.com"
    smtp_password = "tkjs cmsk zzrk vugc"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

    return JsonResponse({"message": "Email sent successfully!"})
