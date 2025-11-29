import schedule
import time
from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)

def send_sms():
    message = client.messages.create(
        body="Reminder: Stay Happy!",
        from_="+1234567890",
        to="+1987654321"
    )
    print("Daily SMS sent:", message.sid)

schedule.every().day.at("09:00").do(send_sms)

while True:
    schedule.run_pending()
    time.sleep(1)
