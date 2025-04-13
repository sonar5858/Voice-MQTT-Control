from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
from_whatsapp_number = os.getenv("TWILIO_FROM")
to_whatsapp_number = os.getenv("TWILIO_TO")

def send_whatsapp_alert(message_text):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_body = f"{message_text}\n⏱️ {now}"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(f"📲 WhatsApp alert sent! SID: {message.sid}")
