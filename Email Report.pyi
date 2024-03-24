import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import getpass
import schedule
import time

def send_email():
    # Get user input
    sender_email = "Raspberrypidreamcoders@gmail.com"
    receiver_email = "a_devrieze@wincoll.ac.uk" #INPUT THE RECIPIENT EMAIL HERE
    png_file_path = "C:/Users/A_devrieze"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Good morning! Here's your daily snoring data file."

    # Attach the PNG file
    with open(png_file_path, 'rb') as fp:
        img_data = fp.read()
        img = MIMEImage(img_data, name="sensor_data.png")
        msg.attach(img)

    # Send the email
    try:
        server = smtplib.SMTP('YOUREMAIL@gmail.com', 587)
        server.starttls()
        password = getpass.getpass("Enter your email password: ")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
schedule.every().day.at("12:00").do(send_email)

