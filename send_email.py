import smtplib
from email.message import EmailMessage
import os


def send_email(image_path, receiver):
	print("Send email function started")
	email_message = EmailMessage()
	email_message["Subject"] = "New person identified!"
	email_message.set_content("A new unknown person was identified in your "
	                          "house.\nCheck if it is someone you know or if "
	                          "it is an intruder!")
	
	with open(image_path, "rb") as file:
		content = file.read()
	
	email_message.add_attachment(content, maintype="image",
	                             subtype="png")

	username = "codspecialops@gmail.com"
	password = os.getenv("PASSWORD")
	
	gmail = smtplib.SMTP("smtp.gmail.com", 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(username, password)
	gmail.sendmail(username, receiver, email_message.as_string())
	gmail.quit()
	print("Send email function ended")
