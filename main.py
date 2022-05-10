from smtplib import SMTP_SSL as SMTP
import json
import time
import random
import os


def setCreds():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    data = {"email": email, "password": password}
    with open('secret.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Get credentials from json file
def creds():
    with open('secret.json', 'r') as f:
        credentials = json.load(f)
    return credentials


# Send email using SMTP trying to avoid spamdetection by using TLS
def send_email(recipient, message):
    server = SMTP("smtp.gmail.com", 465)
    server.ehlo()
    server.starttls
    password = creds()["password"]
    email = creds()["email"]
    server.login(email, password)
    server.sendmail(email, recipient, message)
    print("Email sent!")
    server.quit()


def main():
    recipient = input("Enter recipient email: ")
    message = input("Enter message: ")
    repeat = input("How Many times do you want to send this message? ")
    for i in range(int(repeat)):
        print("Message: ", i + 1)
        timeout = random.uniform(0.2, 2)
        send_email(recipient, message)
        time.sleep(timeout)


# Check if main.py is running as main
if __name__ == '__main__':
    if not os.path.isfile('secret.json'):
        setCreds()
        
    main()
