# bot.py

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import anthropic
import os
from dotenv import load_dotenv

# ------------------------------
# Load environment variables
# ------------------------------
load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL")  # Model comes from .env
GWI_API_BASE_URL = os.getenv("GWI_API_BASE_URL")
GWI_API_USER = os.getenv("GWI_API_USER")
GWI_API_PASSWORD = os.getenv("GWI_API_PASSWORD")

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

app = Flask(__name__)

# ------------------------------
# GWI API Function
# ------------------------------
def get_customer_balance(customerid):
    """
    Fetches customer balance from GWI API with HTTP Basic Auth.
    Returns a formatted string or a friendly error message.
    """
    url = f"{GWI_API_BASE_URL}/customer_balance/{customerid}"
    print(f"[DEBUG] Fetching balance for account {customerid} from {url}")

    try:
        response = requests.get(url, auth=(GWI_API_USER, GWI_API_PASSWORD), timeout=5)
        print(f"[DEBUG] API response status: {response.status_code}")
        print(f"[DEBUG] API response text: {response.text}")

        if response.status_code == 200:
            try:
                data = response.json()
                print(f"[DEBUG] API response JSON: {data}")
            except Exception:
                print("[ERROR] Failed to parse JSON from API response")
                return "Error fetching balance. Please try again later."

            if "message" in data:
                return f"No balance found for account {customerid}."
            else:
                first_name = data.get("FIRST_NAME", "")
                last_name = data.get("LAST_NAME", "")
                balance = data.get("BALLANCE", "0")
                return f"Customer: {first_name} {last_name}\nAccount: {customerid}\nBalance: GYD {balance}"
        elif response.status_code == 401:
            return "Error: Unauthorized to access balance API."
        else:
            return f"Error fetching balance (HTTP {response.status_code})."
    except Exception as e:
        print(f"[ERROR] Failed to fetch balance: {e}")
        return "Error fetching balance. Please try again later."

# ------------------------------
# Webhook Endpoint
# ------------------------------
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body")
    print(f"[DEBUG] Incoming WhatsApp message: {incoming_msg}")

    # Extract numeric account ID from message
    customerid = None
    for w in incoming_msg.split():
        if w.isdigit():
            customerid = w
            break

    if customerid:
        # Call GWI API
        reply = get_customer_balance(customerid)
    else:
        # Use Claude AI for general queries
        message = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are a Guyana Water Inc. WhatsApp assistant.
Help users check their water account balances and answer general queries.
Be short, clear, and professional.

User message:
{incoming_msg}
"""
                }
            ]
        )
        reply = message.content[0].text

    print(f"[DEBUG] Reply to WhatsApp: {reply}")

    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

# ------------------------------
# Optional: Health Check Route
# ------------------------------
@app.route("/", methods=["GET"])
def home():
    return "GWI WhatsApp Bot is running!"

# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
