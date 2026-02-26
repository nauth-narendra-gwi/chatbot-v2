# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    print(f"[DEBUG] Incoming WhatsApp message: {incoming_msg}")

    # Check if message contains a numeric account ID
    customerid = None
    for w in incoming_msg.split():
        if w.isdigit():
            customerid = w
            break

    if customerid:
        # Call GWI API
        reply = get_customer_balance(customerid)
        if not reply:
            reply = "Sorry, we could not find your account or balance."
    else:
        # Fallback to Claude AI for general queries
        message = client.messages.create(
            model= CLAUDE_MODEL,
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


   https://ubuntu.com/aws/pro

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Thu Feb 26 13:33:10 2026 from 18.206.107.27
/usr/bin/xauth:  file /home/ubuntu/.Xauthority does not exist
ubuntu@ip-172-31-31-147:~$ cd whatsapp-bot/
ubuntu@ip-172-31-31-147:~/whatsapp-bot$ ll
total 20
drwxrwxr-x 3 ubuntu ubuntu 4096 Feb 26 13:39 ./
drwxr-x--- 6 ubuntu ubuntu 4096 Feb 26 13:50 ../
-rw-rw-r-- 1 ubuntu ubuntu  226 Feb 26 13:39 .env
-rw-rw-r-- 1 ubuntu ubuntu 3296 Feb 26 13:38 bot.py
drwxrwxr-x 5 ubuntu ubuntu 4096 Feb 26 06:14 venv/
ubuntu@ip-172-31-31-147:~/whatsapp-bot$ nano bot.py
  GNU nano 7.2                                                                                        bot.py *
    print(f"[DEBUG] Incoming WhatsApp message: {incoming_msg}")

    # Check if message contains a numeric account ID
    customerid = None
    for w in incoming_msg.split():
        if w.isdigit():
            customerid = w
            break

    if customerid:
        # Call GWI API
        reply = get_customer_balance(customerid)
        if not reply:
            reply = "Sorry, we could not find your account or balance."
    else:
        # Fallback to Claude AI for general queries
        message = client.messages.create(
            model= CLAUDE_MODEL,
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
