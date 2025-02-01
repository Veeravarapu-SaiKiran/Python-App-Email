from flask import Flask, request, render_template
import smtplib
import os
from email.mime.text import MIMEText

app = Flask(__name__)

# Function to send an email
def send_email(to_email, subject, message):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")  # Use an App Password for security

    if not sender_email or not sender_password:
        return "Email credentials are missing. Set EMAIL_USER and EMAIL_PASS environment variables."

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = request.form.get("num1", type=int)
        num2 = request.form.get("num2", type=int)
        email = request.form.get("email")

        if num1 is None or num2 is None or not email:
            return "Invalid input. Please enter both numbers and an email."

        result = num1 + num2
        message = f"The sum of {num1} and {num2} is {result}."
        
        # Send result via email
        email_status = send_email(email, "Your Addition Result", message)

        return f"Addition Result: {result} <br> {email_status}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
