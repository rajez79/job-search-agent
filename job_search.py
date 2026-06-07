import requests

TOKEN = "7987267470:AAH10nc5oXk1igpLJNTd60yJnY8-7QQAz1Q"
CHAT_ID = "868452309"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "Hello Raja! Testing Telegram Bot."
}

print("URL:", url)

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)