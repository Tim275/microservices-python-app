import smtplib
from email.mime.text import MIMEText

# Use the Gmail address and password from your secret.yaml file
gmail_address = "timour.miagol@gmail.com"
gmail_password = "pdvb eodb eooo wunz"

# Create a text/plain message
msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = gmail_address
msg['To'] = 'timour.miagol@gmail.com'  # Replace with your email address

# Send the message via Gmail's SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_address, gmail_password)
server.send_message(msg)
server.quit()